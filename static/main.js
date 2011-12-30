MT = {};
MT.handleDateChange = function() { alert('ahdle dante ghange');

};
MT.startTimer = function() {


}

MT.addTime = function() { alert('addtime');};

MT.deleteTime = function() { alert('addtime');};

MT.tasks = function() { alert('addtime');};

MT.projects = function() { alert('addtime');};

MT.timer = {started: false};

MT.timer.start = function() {
    MT.timer.started = true;
    MT.timer.start_time = new Date();
    // TODO: load and run the appropriate watch.
    $("#clock").text("0:00");
    
    MT.timer.interval = window.setInterval(MT.timer.repaint, 200);
    
    $("#pause").show().button("refresh");
    $("#start_stop").text("Stop").button("refresh");
};



MT.timer.stop = function() {
    var now = new Date();
    window.clearInterval(MT.timer.interval);
    
    var elapsed = now - MT.timer.start_time;
    //alert("elapsed is " + elapsed);
    // do a request to the interface that will save it.
    jQuery.ajax(
      "/record_time",
        {
            'type' : "POST",
            'data' : {
                'start_time' : MT.timer.start_time.getTime(),
                'end_time' : now.getTime(),
                'elapsed' : elapsed,
                'project_id' : MT.settings.project_id,
                'task_id' : MT.settings.task_id
            }
        }
    );
    $("#pause").hide().button("refresh");
    
    $("#save").show().button("refresh");
};

MT.start_stop = function() {
    if(this.timer.started) {
        MT.timer.stop();    
    } else {
        MT.timer.start();
    }    
};

MT.timer.repaint = function() {
    var elapsed = (new Date()) - MT.timer.start_time;
    
    // TODO: format it. doesn't seem to be basic timedelta math in js.
    var seconds = elapsed / 1000.0;
    
    var hours = 0; var minutes = 0;
    while(seconds >= 60 * 60) {
        hours++;
        seconds = seconds - (60 * 60);
    }
    while(seconds >= 60) {
        minutes++;
        seconds = seconds - 60;
    }
    
    var formattedTime = hours + ":" + minutes.toFixed(0) + ":" + seconds.toFixed(2);
    $("#clock").text(formattedTime);
};