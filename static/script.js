$(function() {
  var dragHandler = function(evt) {
    evt.preventDefault();
  };

  var dropHandler = function(evt) {
    evt.preventDefault();
    var files = evt.originalEvent.dataTransfer.files;

    var reader = new FileReader();

    reader.onload = function(e) {
      $("#uploaded").attr("src", e.target.result);
    };

    reader.readAsDataURL(files[0]);

    var formData = new FormData();
    formData.append("file2upload", files[0]);

    var req = {
      url: "/sendfile",
      method: "post",
      processData: false,
      contentType: false,
      data: formData
    };

    var promise = $.ajax(req);
  };

  var dropHandlerSet = {
    dragover: dragHandler,
    drop: dropHandler
  };

  $(".droparea").on(dropHandlerSet);
});
