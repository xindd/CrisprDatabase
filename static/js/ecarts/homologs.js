// var pathSymbols = {
//     reindeer: '../../imgs/details_open.png',
//     plane: '../../imgs/details_close.png'
// };
// var hours = ['-5', '-4', '-3', '-2', '-1',
//         '0', '1', '2', '3', '4', '5'];
// var proteinid = 'homol1';
//
// var data = [[0,0,5],[0,1,1],[0,2,10],[0,3,4],[0,4,6],[0,5,2],[0,6,6],[0,7,2],[0,8,1],[0,9,3],[0,10,4]];
//
// var sy='../../imgs/details_open.png';

function homologs(proteinid, data, divid) {
    var pathSymbols = {
    rightblue: 'image:///../static/imgs/right.png',
    leftblue: 'image:///../static/imgs/left.png',
    rightred: 'image:///../static/imgs/rightred.png',
    leftred: 'image:///../static/imgs/leftred.png',
    leftnone: 'image:///../static/imgs/leftnone.png',
    rightnone: 'image:///../static/imgs/leftnone.png',
    rightanti: 'image:///../static/imgs/rightanti.png',
    leftanti: 'image:///../static/imgs/leftanti.png',

    };
    var hours = ['','','','','','','','','','',''];
    var sy='image:///../static/imgs/left.png';
    var datac=[];
    for(var d=0;d<data.length; d++)
    {

        hours[data[d][5]-1] = data[d][2]
        if(data[d][3]=='(+)'){
            if(data[d][4]=='yes'){
                if(data[d][2] == ''){
                    sy = pathSymbols.rightnone;
                }else {
                    sy = pathSymbols.rightred;
                }
            }else{
                if(data[d][2] == ''){
                    sy = pathSymbols.rightnone;
                }else if(data[d][2].indexOf('HTH')>-1){
                    sy = pathSymbols.rightanti;
                }else if(data[d][2].indexOf('Acr')>-1){
                    sy = pathSymbols.rightred;
                }else {
                   sy = pathSymbols.rightblue;
                }

            }
        }
        else{
            if(data[d][4]=='yes'){
                if(data[d][2] == ''){
                    sy = pathSymbols.leftnone;
                }else {
                   sy = pathSymbols.leftred;
                }

            }else{
                if(data[d][2] == ''){
                    sy = pathSymbols.leftnone;
                }else if(data[d][2].indexOf('HTH')>-1){
                    sy = pathSymbols.leftanti;
                }else if(data[d][2].indexOf('Acr')>-1){
                    sy = pathSymbols.leftred;
                }else {
                   sy = pathSymbols.leftblue;
                }

            }
        };
        datac.push({
            name: data[d][2],
            value:[data[d][5]-1],
            symbol:sy,
        });
    }
    var option = {
        tooltip: {
            position: 'top'
        },
        title: [{
            show: false,
            textBaseline: 'middle',
            // top: (0 + 0.5) * 100 / 7 + '%',
            text: proteinid,

        }],
        xAxis: {
            show:false,
            type: 'category',
            data: hours,
             axisLine: {
                show: false,
            },
            axisTick: {
            },
        },
        yAxis: {
            type: 'category',
            show:false
        },
        grid: {
        bottom: 10,
        top: 0,
    },
        series: [
            {
            type: 'scatter',
            data: datac,
                label: {
                normal: {
                    show: true,
                    color: '#000',
                    formatter: function(data) {
                        return data.data.name}

                }
            },
            // label: {
            //     normal: {
            //         position:['10%', '-10%'],
            //         show: true,
            //         formatter: '{b}',
            //         rotate:15
            //     }
            // },
                symbolSize: 36
            }
            ]
    };
    var mychart = echarts.init(document.getElementById(divid))
    mychart.setOption(option)
}


