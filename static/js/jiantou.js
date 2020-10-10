
function jiantou(proteinid, data, divid) {
    // data=[{'name':"Documents",'value':[0, 3, 4, '+']},
    // {'name':"Nodes",'value':[0, 1, 2, '+']},
    // {'name':"Documents",'value':[0, 6, 8, '-']},
    // ]
    seriesdata=[];
    for(var d=0;d<data.length;d++){
        var col = '#2744729e'
        if(data[d].center == 'center'){
            col = '#ff5656b3'
        }
        seriesdata.push(
            {
                type: 'custom',
                itemStyle: {
                    normal: {
                        color:col
                    }
                },
                label: {
                    normal: {
                        // formatter: '{b}',
                        // position: 'center',
                        show: true
                    },
                },
                encode: {
                    x: [1, 2],
                    y: 0
                },
                data: [data[d]],
                renderItem: renderItem,
            }
        )
    }
    function renderItem(params, api) {
        var categoryIndex = api.value(0);
        var start = api.coord([api.value(1), categoryIndex]);
        var end = api.coord([api.value(2), categoryIndex]);
        rightpoints = {
          p1: [start[0], start[1]+api.size([0, 1])[1] *0.15],
          p2: [start[0], start[1]-api.size([0, 1])[1] *0.15],
          p3: [end[0]-(end[0]-start[0])*0.4, start[1]-api.size([0, 1])[1] *0.15],
          p4: [end[0]-(end[0]-start[0])*0.4, start[1]-api.size([0, 1])[1] *0.25],
          p5: [end[0], start[1]],
          p6: [end[0]-(end[0]-start[0])*0.4, start[1]+api.size([0, 1])[1] *0.25],
          p7: [end[0]-(end[0]-start[0])*0.4, end[1]+api.size([0, 1])[1] *0.15],
        }
        leftpoints = {
          p1: [start[0], start[1]],
          p2: [start[0]+ (end[0]-start[0])*0.4, start[1]-api.size([0, 1])[1] *0.25],
          p3: [start[0]+ (end[0]-start[0])*0.4, start[1]-api.size([0, 1])[1] *0.15],
          p4: [end[0], start[1]-api.size([0, 1])[1] *0.15],
          p5: [end[0], start[1]+api.size([0, 1])[1] *0.15],
          p6: [start[0]+ (end[0]-start[0])*0.4, start[1]+api.size([0, 1])[1] *0.15],
          p7: [start[0]+ (end[0]-start[0])*0.4, end[1]+api.size([0, 1])[1] *0.25],
        }
        if(api.value(3)=='(+)'){
            points=rightpoints
        }else if(api.value(3)=='(-)'){
            points=leftpoints
        }
        return {
            type: 'polygon',
            shape: {
                points: [points.p1,points.p2,points.p3,points.p4,points.p5,
                points.p6,points.p7,points.p1]
            },
            style: api.style(),
        }

    }
    option = {
        tooltip: {
            formatter: function (params) {
                return params.marker + params.name + ': ' + params.value[3];
            }
        },
        title: {
            show: false,
            text: 'Profile',
            left: 'center'
        },
        grid: {
            top:0,
           bottom: 0,
        },
        xAxis: {
            show:false,
            // type: 'value',
            // data: [1,2,3,4,5,6,7,8,9,10]
        },
        yAxis: {
            show:false,
            type: 'category',
            data: ''
        },
        series: seriesdata
            // [
        //     {
        //     type: 'custom',
        //     itemStyle: {
        //         normal: {
        //             opacity: 0.8
        //         }
        //     },
        //     encode: {
        //         x: [1, 2],
        //         y: 0
        //     },
        //     data: data,
        //     renderItem: renderItem,
        // }
        // ]
    };
    var mychart = echarts.init(document.getElementById(divid))
    mychart.setOption(option)
}