let labes1 = ['Yes', 'Yes by in green'];
let data1 = [69, 31]
let colors1 = ['yellow', 'green']

let myChart1 = document.getElementById("myChart").getContext('2d');

let chart1 = new Chart(myChart1, {
    type: 'doughnut',
    data {
        labels: labels1, 
        datasets: [ {
            data: data1, 
            backgroundColor: colors1
        }]
    },
    options: {
        title: {
            text: "Do you like doughnuts?",
            display: true
        }
    }

});