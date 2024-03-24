let num = 4;

document.addEventListener("DOMContentLoaded", function () {

    const scroll = document.getElementById('scroll');

    scroll.addEventListener('click', function () {
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    let timeline = document.querySelector('.timeline');

    function createTimelineItem() {
        let item = document.createElement('div');
        item.classList.add('timeline-item');

        let h4 = document.createElement('h4');
        h4.textContent = 'String';
        item.appendChild(h4);

        let timelineCheck = document.createElement('div');
        timelineCheck.classList.add('timeline-check');


        timelineCheck.addEventListener('click', function (event) {
            item.classList.toggle('timeline-item-complete');
            let checkIcon = timelineCheck.querySelector('svg:last-child path');
            checkIcon.classList.toggle('circle');
            let text = item.querySelector('h4, p');
            text.classList.toggle('complete-text');
        });

        item.appendChild(timelineCheck);

        let timelineBox = document.createElement('div');
        timelineBox.classList.add('timeline-box');

        let p = document.createElement('p');
        p.textContent = '(Resource Name) will teach you (description)';
        timelineBox.appendChild(p);

        item.appendChild(timelineBox);

        return item;
    }


    function addTimelineItems(num) {
        for (let i = 0; i < num; i++) {
            timeline.appendChild(createTimelineItem());
        }
    }

    addTimelineItems(num); // Change the number to create as many timeline items as desired

});

