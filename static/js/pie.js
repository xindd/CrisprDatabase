
function pie(title,legend,data) {
    // var title = '同名数量统计'
    // var legend =  ['CARD','U盘',,'SSD','U盘','嵌入式','FLASH']
    // var data = [
    //     {value: 45,name: 'CARD'}, {
    //             value: 25,
    //             name: 'SSD'
    //         }, {
    //             value: 15,
    //             name: 'U盘'
    //         }, {
    //             value: 8,
    //             name: '嵌入式'
    //         }, {
    //             value: 7,
    //             name: 'FLASH'
    //         }
    //         ]
    option = {
        // title : {
        //     text: title,
        //     x:'center'
        // },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            type: 'scroll',
            // orient: 'vertical',
            //             // right: 10,
            //             // top: 20,
            bottom: 0,
            data: legend,

            selected: data.selected
        },
        series: [{
            name: '',
            type: 'pie',
            radius: '68%',
            center: ['50%', '50%'],
            clockwise: false,
            data: data,
            label: {
                normal: {
                    textStyle: {
                        color: '#999',
                        fontSize: 14,

                    },
                    formatter: function(param) {
                         return param.name + ':\n' + Math.round(param.percent) + '%';
                     }
                }
            },
            labelLine: {
                 normal: {
                     smooth: true,
                     lineStyle: {
                         width: 2
                     }
                 }
             },
            itemStyle: {
                normal: {
                    borderWidth: 4,
                    borderColor: '#ffffff',
                },
                emphasis: {
                    borderWidth: 0,
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }],
        color: [
            '#00acee',
            '#52cdd5',
            '#79d9f1',
            '#a7e7ff',
            '#c8efff'
        ],
        backgroundColor: '#fff'
    };
    return option;
}
