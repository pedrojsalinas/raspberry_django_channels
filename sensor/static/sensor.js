$(function() {
  // When we're using HTTPS, use WSS too.
  var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
  var chatsock = new ReconnectingWebSocket(
    ws_scheme + "://" + window.location.host + "/sensor/"
  );

  chatsock.onopen = function() {
    console.log("Connected!");
    $("#sensor").text("Connected!");
    chatsock.send("Connected!");
  };

  chatsock.onmessage = function(message) {
    if (message.data=="1") {
      $("#sensor").text(message.data);
    }else if (message.data=="2") {
      $("#sensor2").text(message.data);
    }
  };
});
