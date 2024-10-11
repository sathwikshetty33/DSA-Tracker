let st = document.getElementById('start');
let end = document.getElementById('end');
let e = document.getElementById('e');
let em = document.getElementById('em');
let m = document.getElementById('m');
let mm = document.getElementById('mm');
let h = document.getElementById('h');
let hm = document.getElementById('hm');
let re = document.getElementById('reset');
let sub=document.getElementById('submit')
let m1 = 0, m2 = 0, m3 = 0;
let con = false;
let startTime;
let elapsedTime = 0;  // Store elapsed time when paused
let hrString = "00", minString = "00", secString = "00"; // Example time values
// Update task display counts
function updateTaskCounts() {
    document.getElementById('easym').innerHTML = m1;
    document.getElementById('mediumm').innerHTML = m2;
    document.getElementById('hardm').innerHTML = m3;
}
function resetTimeDisplay() {
    document.getElementById('hr').innerHTML = "00";
    document.getElementById('min').innerHTML = "00";
    document.getElementById('sec').innerHTML = "00";
    document.getElementById('count').innerHTML = "00";
}


document.getElementById('taskForm').addEventListener('submit', function(event) {

    document.getElementById('easy').value = m1;  // Update m1, m2, m3 accordingly
    document.getElementById('medium').value = m2;
    document.getElementById('hard').value = m3;
    const t=document.getElementById('takentime');
    t.value = (hrString + ":" + minString + ":" + secString);
    const now = new Date();

    // Set the current date in YYYY-MM-DD format
    const dateField = document.getElementById('date');
    const currentDate = now.toISOString().split('T')[0]; // Extract date part
    dateField.value = currentDate;

    // Set the current time in HH:MM:SS format
    const submittimeField = document.getElementById('submittime');
    const currentTime = now.toTimeString().split(' ')[0]; // Extract time part
    submittimeField.value = currentTime;

    console.log("Easy:", m1, "Medium:", m2, "Hard:", m3, "Time:", document.getElementById('time').value);
    alert("Success");

});

st.addEventListener('click', function () {
    if (!con) {
        con = true;
        startTime = Date.now() - elapsedTime;  // Continue from the last paused point
        time();  // Start the timer
    }
});

// End the timer
end.addEventListener('click', function () {
    con = false;  // Pause the timer
    elapsedTime = Date.now() - startTime;  // Store elapsed time for resuming
});

// Reset all values and display
re.addEventListener('click', function () {
    // Reset task counts and elapsed time
    con = false;
    m1 = m2 = m3 = 0;  // Reset task counts
    elapsedTime = 0;  // Reset elapsed time

    // Reset the display values
    resetTimeDisplay();
    updateTaskCounts();
});

// Increase "easy" count
e.addEventListener('click', function () {
    if (con) {
        m1++;
        updateTaskCounts();  // Update the display
    }
});

// Decrease "easy" count
em.addEventListener('click', function () {
    if (con) {
        m1 = Math.max(0, m1 - 1);  // Prevent negative values
        updateTaskCounts();  // Update the display
    }
});

// Increase "medium" count
m.addEventListener('click', function () {
    if (con) {
        m2++;
        updateTaskCounts();  // Update the display
    }
});

// Decrease "medium" count
mm.addEventListener('click', function () {
    if (con) {
        m2 = Math.max(0, m2 - 1);  // Prevent negative values
        updateTaskCounts();  // Update the display
    }
});

// Increase "hard" count
h.addEventListener('click', function () {
    if (con) {
        m3++;
        updateTaskCounts();  // Update the display
    }
});

// Decrease "hard" count
hm.addEventListener('click', function () {
    if (con) {
        m3 = Math.max(0, m3 - 1);  // Prevent negative values
        updateTaskCounts();  // Update the display
    }
});

// Timer function
// Timer function
function time() {
    if (con) {
        let currentTime = Date.now();
        let diff = currentTime - startTime;  // Calculate elapsed time in milliseconds

        // Convert elapsed time into hours, minutes, seconds, and centiseconds
        hr = Math.floor(diff / (1000 * 60 * 60));
        min = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        sec = Math.floor((diff % (1000 * 60)) / 1000);
        co = Math.floor((diff % 1000) / 10);  // 10 ms intervals for centiseconds

        // Format time display
        hrString = hr < 10 ? "0" + hr : hr;
        minString = min < 10 ? "0" + min : min;
        secString = sec < 10 ? "0" + sec : sec;
        countString = co < 10 ? "0" + co : co;

        // Update the timer display on the webpage
        document.getElementById('hr').innerHTML = hrString;
        document.getElementById('min').innerHTML = minString;
        document.getElementById('sec').innerHTML = secString;
        document.getElementById('count').innerHTML = countString;

        // Update the hidden input field with the time value
        document.getElementById('takentime').value = hrString + ":" + minString + ":" + secString;
        console.log(hrString + ":" + minString + ":" + secString)
        // Recursively call time() to keep the timer running
        requestAnimationFrame(time);  // Use requestAnimationFrame for smoother updates
    }
}
