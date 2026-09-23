document.addEventListener('DOMContentLoaded', () => {
  const dropzone = document.getElementById('dropzone');
  const fileInput = document.getElementById('file-input');
  const statusBox = document.getElementById('status-box');
  const progressBar = document.getElementById('progress-bar');
  const statusText = document.getElementById('status-text');
  const progressPercent = document.getElementById('progress-percent');
  const alertContainer = document.getElementById('alert-container');

  const previewPlaceholder = document.getElementById('preview-placeholder');
  const previewContent = document.getElementById('preview-content');
  const previewImg = document.getElementById('preview-img');

  const metaDocId = document.getElementById('meta-doc-id');
  const metaFilename = document.getElementById('meta-filename');
  const metaSize = document.getElementById('meta-size');
  const metaDimensions = document.getElementById('meta-dimensions');
  const metaMode = document.getElementById('meta-mode');
  const metaChecksum = document.getElementById('meta-checksum');
  const metaReadability = document.getElementById('meta-readability');

  // Drag and Drop Event Listeners
  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.add('dragover');
    }, false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.remove('dragover');
    }, false);
  });

  dropzone.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileUpload(files[0]);
    }
  });

  fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
      handleFileUpload(e.target.files[0]);
    }
  });

  function showAlert(message, type = 'error') {
    alertContainer.innerHTML = `
      <div class="alert alert-${type}">
        <span>${type === 'error' ? '⚠️' : '✓'}</span>
        <div>${message}</div>
      </div>
    `;
  }

  function clearAlert() {
    alertContainer.innerHTML = '';
  }

  function formatBytes(bytes, decimals = 2) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
  }

  function handleFileUpload(file) {
    clearAlert();
    statusBox.style.display = 'block';
    progressBar.style.width = '0%';
    progressPercent.textContent = '0%';
    statusText.textContent = `Uploading ${file.name}...`;

    const formData = new FormData();
    formData.append('file', file);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/upload', true);

    xhr.upload.onprogress = (e) => {
      if (e.lengthComputable) {
        const percent = Math.round((e.loaded / e.total) * 100);
        progressBar.style.width = `${percent}%`;
        progressPercent.textContent = `${percent}%`;
        if (percent === 100) {
          statusText.textContent = 'Validating document readability...';
        }
      }
    };

    xhr.onload = function () {
      statusBox.style.display = 'none';
      if (xhr.status === 201) {
        const response = JSON.parse(xhr.responseText);
        showAlert('Document uploaded and validated successfully!', 'success');
        renderDocumentPreview(response.document);
      } else {
        let errorMsg = 'Failed to upload document.';
        try {
          const errData = JSON.parse(xhr.responseText);
          errorMsg = errData.detail || errorMsg;
        } catch (e) {}
        showAlert(errorMsg, 'error');
      }
    };

    xhr.onerror = function () {
      statusBox.style.display = 'none';
      showAlert('Network error occurred while uploading document.', 'error');
    };

    xhr.send(formData);
  }

  function renderDocumentPreview(doc) {
    previewPlaceholder.style.display = 'none';
    previewContent.style.display = 'block';

    previewImg.src = `/api/upload/${doc.document_id}/preview`;

    metaDocId.textContent = doc.document_id;
    metaFilename.textContent = doc.original_filename;
    metaSize.textContent = formatBytes(doc.file_size_bytes);
    
    const details = doc.readability_details || {};
    metaDimensions.textContent = `${details.width || 0} × ${details.height || 0} px`;
    metaMode.textContent = `${details.format || 'IMG'} / ${details.mode || 'RGB'} (${details.channels || 3} Ch)`;
    metaChecksum.textContent = doc.sha256_checksum ? doc.sha256_checksum.substring(0, 24) + '...' : '-';

    if (doc.is_readable) {
      metaReadability.className = 'badge badge-success';
      metaReadability.textContent = 'Valid for OCR';
    } else {
      metaReadability.className = 'badge badge-danger';
      metaReadability.textContent = 'Unreadable';
    }
  }
});
