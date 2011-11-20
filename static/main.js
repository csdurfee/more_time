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
    // load and run the appropriate watch.
    var watch = MT.watch_face(MT.id);

    watch.start(0);
    
};

MT.timer.stop = function() {
    var now = new Date();
    var elapsed = now - MT.timer.start_time;
    alert("elapsed is " + elapsed);
    // do a request to the interface that will save it.
    jQuery.ajax(
      "/record_time",
        {
            'type' : "POST",
            'elapsed' : elapsed,
            'project_id' : MT.project_id,
            'task_id' : MT.task_id
        }
    );
};

MT.start_stop = function() {
    if(this.timer.started) {
        MT.timer.stop();    
    } else {
        MT.timer.start();
    }    
};

MT.watches = {};

MT.watches.generic = function(id) {
    var watch = {id:id};

    // init code here.

    watch.start = function(startTime) {
        $("#clock").text(this.renderTime(startTime));
    };

    watch.renderTime = function(rawTime) {
        return "pants:" + rawTime;  
    };

    watch.run = function() {
        alert('fooby');
    };
    
    watch.listen = function() {
        
        
    };
    return watch;
    
};

// TODO: load based on prefs.
MT.watch_face = MT.watches.generic;