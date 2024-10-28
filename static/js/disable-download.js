// Function to check if a URL is for a PDF or PPTX file
function isRestrictedFile(url) {
  const lowercaseUrl = url.toLowerCase();
  return (
      // Check file extensions
      lowercaseUrl.endsWith('.pdf') ||
      lowercaseUrl.endsWith('.pptx') ||
      // Check MIME types
      lowercaseUrl.includes('application/pdf') ||
      lowercaseUrl.includes('application/vnd.openxmlformats-officedocument.presentationml.presentation')
  );
}

// Function to prevent restricted file downloads
function preventFileDownloads() {
  // Intercept all clicks on the document
  document.addEventListener('click', function(event) {
      const target = event.target;

      // Check if the clicked element is a link or is inside a link
      const link = target.closest('a');
      if (link && link.href) {
          if (isRestrictedFile(link.href)) {
              // Prevent the default download behavior
              event.preventDefault();

              // Show a message to the user
              alert('Downloading PDF and PowerPoint files is disabled.');

              // Log the attempted download
              console.log('Prevented download of restricted file:', link.href);
              return false;
          }
      }
  }, true);

  // Intercept form submissions
  document.addEventListener('submit', function(event) {
      const form = event.target;
      if (form.action && isRestrictedFile(form.action)) {
          event.preventDefault();
          alert('Downloading PDF and PowerPoint files is disabled.');
          console.log('Prevented form submission to restricted file:', form.action);
          return false;
      }
  }, true);

  // Block downloads initiated through XMLHttpRequest
  const originalXHR = window.XMLHttpRequest.prototype.open;
  window.XMLHttpRequest.prototype.open = function(method, url) {
      if (isRestrictedFile(url)) {
          throw new Error('Downloading PDF and PowerPoint files is disabled.');
      }
      return originalXHR.apply(this, arguments);
  };

  // Block downloads initiated through Fetch API
  const originalFetch = window.fetch;
  window.fetch = function(resource, init) {
      if (typeof resource === 'string' && isRestrictedFile(resource)) {
          return Promise.reject(new Error('Downloading PDF and PowerPoint files is disabled.'));
      }
      // Handle Request objects
      if (resource instanceof Request && isRestrictedFile(resource.url)) {
          return Promise.reject(new Error('Downloading PDF and PowerPoint files is disabled.'));
      }
      return originalFetch.apply(this, arguments);
  };

  // Disable drag and drop of files
  document.addEventListener('dragover', function(event) {
      event.preventDefault();
  }, false);

  document.addEventListener('drop', function(event) {
      event.preventDefault();
      const items = event.dataTransfer.items;
      for (let item of items) {
          if (item.type === 'application/pdf' ||
              item.type === 'application/vnd.openxmlformats-officedocument.presentationml.presentation') {
              alert('Dropping PDF and PowerPoint files is disabled.');
              return false;
          }
      }
  }, false);
}

// Add Content Security Policy to block file downloads
function addCSPHeader() {
  const meta = document.createElement('meta');
  meta.httpEquiv = 'Content-Security-Policy';
  meta.content = "default-src 'self'; object-src 'none'; plugin-types application/x-shockwave-flash;";
  document.head.appendChild(meta);
}

// Disable right-click on specific file types
function disableRightClick() {
  document.addEventListener('contextmenu', function(event) {
      const target = event.target;
      const link = target.closest('a');
      if (link && link.href && isRestrictedFile(link.href)) {
          event.preventDefault();
          return false;
      }
  }, true);
}

// Initialize all prevention mechanisms
document.addEventListener('DOMContentLoaded', function() {
  preventFileDownloads();
  addCSPHeader();
  disableRightClick();
  console.log('PDF and PPTX download prevention initialized');
});

// Disable browser PDF viewer
function disablePDFViewer() {
  const meta = document.createElement('meta');
  meta.name = 'forcePDFDownload';
  meta.content = 'noInline';
  document.head.appendChild(meta);
}
