$(function() {

    var list = $( "#input_data" ).text();
    var clean1 = list.replace("[", "");
    var clean2 = clean1.replace("]", "");
    var clean3 = clean2.replace("'", "");
    var clean4 = clean2.replace("'", "");

    final = clean4.split(",");

    document.getElementById("song1").innerHTML =  final[0];
    document.getElementById("song2").innerHTML = final[1];
    document.getElementById("song3").innerHTML = '<a class="displaybutton2"href=' + final[2] + '>' + 'play on spotify' + '</a>';
    document.getElementById("artist1").innerHTML =  final[3];
    document.getElementById("artist2").innerHTML = final[4];
    document.getElementById("artist3").innerHTML = '<a class="displaybutton2"href=' + final[5] + '>' + 'play on spotify' + '</a>';
    document.getElementById("link1").innerHTML =  final[6];
    document.getElementById("link2").innerHTML = final[7];
    document.getElementById("link3").innerHTML = '<a class="displaybutton2"href=' + final[8] + '>' + 'play on spotify' + '</a>';
    
    
    
    // var dragHandler = function(evt){
    //     evt.preventDefault();
    // };

    // var dropHandler = function(evt){
    //     evt.preventDefault();
    //     var files = evt.originalEvent.dataTransfer.files;

    //     var formData = new FormData();
    //     formData.append("file2upload", files[0]);

    //     var req = {
    //         url: "/sendfile",
    //         method: "post",
    //         processData: false,
    //         contentType: false,
    //         data: formData
    //     };

    //     var promise = $.ajax(req);
    // };

    // var dropHandlerSet = {
    //     dragover: dragHandler,
    //     drop: dropHandler
    // };

    // $(".droparea").on(dropHandlerSet);
});