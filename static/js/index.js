//$() 页面加载完后，执行
//页面上所有的js动态效果都写在这里

//空调概况
$(function(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector('.overview .echarts .overview_bar'));
    var data = [
        {
            name: '故障率',
            value: 54
        },{
            name: '空调使用率',
            value: 44
        },{
            name: 'MTBF',
            value: 35
        },{
            name: '车辆在线率',
            value: 30
        }]
        
        var titleArr= [], seriesArr=[];
        colors=[['#389af4', '#dfeaff'],['#ff8c37', '#ffdcc3'],['#ffc257', '#ffedcc'], ['#fd6f97', '#fed4e0'],['#a181fc', '#e3d9fe']]
        data.forEach(function(item, index){
            titleArr.push(
                {
                    text:item.name,
                    left: index * 20 + 18 +'%',
                    top: '75%',
                    textAlign: 'center',
                    textStyle: {
                        fontWeight: 'normal',
                        fontSize: '16',
                        color: colors[index][0],
                        textAlign: 'center',
                    },
                }        
            );
            seriesArr.push(
                {
                    name: item.name,
                    type: 'pie',
                    clockWise: false,
                    radius: [25, 35],
                    itemStyle:  {
                        normal: {
                            color: colors[index][0],
                            shadowColor: colors[index][0],
                            shadowBlur: 0,
                            label: {
                                show: false
                            },
                            labelLine: {
                                show: false
                            },
                        }
                    },
                    hoverAnimation: false,
                    center: [index * 20 + 20 +'%', '40%'],
                    data: [{
                        value: item.value,
                        label: {
                            normal: {
                                formatter: function(params){
                                    return params.value+'%';
                                },
                                position: 'center',
                                show: true,
                                textStyle: {
                                    fontSize: '20',
                                    fontWeight: 'bold',
                                    color: colors[index][0]
                                }
                            }
                        },
                    }, {
                        value: 100-item.value,
                        name: 'invisible',
                        itemStyle: {
                            normal: {
                                color: colors[index][1]
                            },
                            emphasis: {
                                color: colors[index][1]
                            }
                        }
                    }]
                }    
            )
        });
       
        
   var option = {
     
        title:titleArr,
        series: seriesArr
    }
   
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
});


// 入口函数--空调告警分布统计
$(function(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector('.fault_stas .echarts .distribute'));

    // 指定图表的配置项和数据
    var option = {
        color: ['#006cff','#60cda0','#ed8884','#ff9f7f','#00g6ff','#9fe6b8','#32c5e9','#1d9dff'],
        // backgroundColor: '#2c343c',
    
        // title: {
        //     text: 'Customized Pie',
        //     left: 'center',
        //     top: 20,
        //     textStyle: {
        //         color: '#ccc'
        //     }
        // },
    
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)',
            position:function(point){
               //  point表示当前鼠标的位置
               // point[0] 鼠标当前这一点x轴的位置
               // point[1] 鼠标当前这一点Y轴的位置
               return [point[0]+10,point[1]+10]
            }
        },
    
        // visualMap: {
        //     show: false,
        //     min: 80,
        //     max: 600,
        //     inRange: {
        //         colorLightness: [0, 1]
        //     }
        // },
        
        series: [
            {
                name: '分布统计',
                type: 'pie',
                //饼图半径，第一个是内半径，第二个是外半径
                radius: [18,80],
                //饼图的中心位置
                center: ['50%', '50%'],
                
                data: [
                    {value: 300, name: '高压故障'},
                    {value: 310, name: '制冷效果差'},
                    {value: 274, name: '制热效果差'},
                    {value: 335, name: '车厢过冷'},
                    {value: 300, name: '温度传感器失效'},
                    {value: 400, name: '车厢过热'},
                    {value: 500, name: '排气温度过高'},
                ],
                //根据数据进行排序
                // .sort(function (a, b) { return a.value - b.value; })
                
                //根据值得大小，确定半径大小，注释的话大小是一样的
                roseType: 'radius',
                
                //图表上文字的颜色如果不设置根图表的颜色一致
                // label: {
                //     color: 'rgba(255, 255, 255, 0.3)'
                // },
                labelLine: {
                    //引导线样式
                    // lineStyle: {
                    //     color: 'rgba(255, 255, 255, 0.3)'
                    // },
                    //平滑度
                    // smooth: 0.2,
                    // 线的长度
                    length: 5,
                    length2: 10
                },
                itemStyle: {
                    //每一个图例的样式
                    // 颜色 默认从全局调色盘
                    // color: red,
                    shadowBlur: 200,
                    //图形阴影的模糊大小
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                },
    
                animationType: 'scale',
                animationEasing: 'elasticOut',
                animationDelay: function (idx) {
                    return Math.random() * 200;
                }
            }
        ]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
});

//入口函数--趋势分析
$(function(){

    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector('.trend1  .temper_trend'));

    var data=[
        [
            [24,40,101,134,90,230,210,230,120,230,210,120],
            [40,64,191,324,290,330,310,213,180,200,180,79],
            [70,64,100,267,290,108,257,244,86,118,180,95],
        ],
        [
            [23,75,12,197,21,67,98,21,43,64,76,38],
            [43,31,65,23,78,21,82,64,43,60,19,34],
            [32,54,34,87,32,45,62,268,93,54,54,24]
        ],
        [
            [34,87,32,76,98,12,32,487,39,36,29,36],
            [56,43,98,21,56,87,143,12,43,54,12,98],
            [43,73,463,54,91,54,84,43,86,43,54,53],
        ],
        [
            [43,73,463,54,91,54,84,43,86,43,54,53],
            [32,54,34,87,32,45,62,268,93,54,54,24],
            [34,87,32,76,98,12,32,487,39,36,29,36],
        ],

    ]

    var option = {
        //图表标题
        title: {
            text: '单位 ℃',
            // subtext: '纯属虚构'
            textStyle:{
                color:'#4996f5'
            },
            left:30,
            top:10
        },
        tooltip: {
            // trigger: 'axis'
        },
        //图例组件，和series里面的每一项对应
        legend: {
            data: ['系统1回风温度', '系统1吸气温度','蒸发器1出口温度'],
              textStyle:{
                color:'#4995f4'
            },
            right:5,
            top:10  
        },

        grid:{
            left:'3%',
            right:'4%',
            bottom:'3%',
            top:'30%',
            containLabel:true
        },
        // toolbox: {
        //     show: true,
        //     feature: {
        //         dataZoom: {
        //             yAxisIndex: 'none'
        //         },
        //         dataView: {readOnly: false},
        //         magicType: {type: ['line', 'bar']},
        //         restore: {},
        //         saveAsImage: {}
        //     }
        // },
        
        //x轴
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月','8月','9月','10月','11月','12月'],
            
            //x轴刻度
            axisTick:{
                show:false
            },
            
            // x轴文本
            axisLabel:{
                color:'#438be5',
                //文本和轴线对齐方式
                align:'left'
            },
            
            //x轴轴线
            axisLine:{
                lineStyle:{
                    color:'#012b48'
                }
            }
            
        },
        
        //y轴
        yAxis: {
            type: 'value',
            
            //y轴最大值
            max:500,
            //y轴最小间隔
            minInterval:100,
            axisLabel: {
                // formatter: '{value}'
                color:'#438be5'
            },
            
             //y轴刻度
            axisTick:{
                show:false
            },
            
             //y轴轴线
            axisLine:{
                lineStyle:{
                    color:'#012b48'
                }
            },
            //y轴分割线
            splitLine:{
                lineStyle:{
                    color:'#012b48'
                }
            }
            
        },
        
        //图例本身设置
        series: [
            {
                name: '系统1回风温度',
                type: 'line',
                //是否平滑
                smooth:true,
                data: [24, 40, 101, 134,90,230,210,230,120,230,210,120],
                
                //标记点，显示最大值最小值得
                // markPoint: {
                //     data: [
                //         {type: 'max', name: '最大值'},
                //         {type: 'min', name: '最小值'}
                //     ]
                // },
                
                //标记线  平均线
                // markLine: {
                //     data: [
                //         {type: 'average', name: '平均值'}
                //     ]
                // }
                
                // //线条颜色设置
                // lineStyle:{
                //     color:'red'
                // },
                
                //拐点样式设置
                itemStyle:{
                    color:'red'
                },
                
                //拐点的大小
                symbolSize:8
                
                //如果2个不一样就分开设置，如果两个一样就设置一个就好了
            },
            {
                name: '系统1吸气温度',
                type: 'line',
                smooth:true,
                //拐点的大小
                symbolSize:8,
                  //拐点样式设置
                itemStyle:{
                    color:'green'
                },
                data: [40,64,191,324,290,330,310,213,180,200,180,79],
                
            },
            {
                name: '蒸发器1出口温度',
                type: 'line',
                smooth:true,
                //拐点的大小
                symbolSize:8,
                  //拐点样式设置
                itemStyle:{
                    color:'blue'
                },
                data: [30,54,80,22,10,15,60,130,100,200,90,35],
                
            }
        ]
    }; 
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);

    // 启动定时刷新图表数据
    var index=0;
    // 申明一个计时器
    setInterval(function(){
        // 1.数组下标++切换数据
        index++;
        if(index>3){
            index=0;
        };

        //2.替换数据
        option.series[0].data=data[index][0];
        option.series[1].data=data[index][1];
        option.series[2].data=data[index][2];
        // 3.重新渲染echarts图表
        myChart.setOption(option)

        // $('.sales .head a').eq(index).addClass('active').siblings('a').removeClass('active')
    },2000);
});

// 入口函数 ---设备监控
$(function(){
    //1.设备监控模块（1.2）有一个tab栏切换

    //   页签设置点击事件
    $('.monitor .tabs a').on('click',function(){
        // 当前点击的页签添加active类，其他的兄弟页签移除这个类
        $(this).addClass('active').siblings().removeClass('active');

        // 获取当前点击的页签索引 
        var idx=$(this).index();
        console.log(idx)
        // 索引一直的页面显示 
        $('.monitor .content').eq(idx).show().siblings('.content').hide();
    })
    //2. 设备监控模块(1.2)有一个轮播图的效果
    // 2.1 必须要理解的轮播图
    // function lunbo(){
    //     $('.monitor .content .carousel ul').animate({
    //         top:-175
    //     },5000,'linear',function(){
    //         $('.monitor .content .carousel ul').css('top',0)
    //     });
    // };

    // lunbo();
    // setInterval(lunbo,5000);

    // 2.2  升级版轮播图

    function lunbo(){
        $('.monitor .content .carousel ul').animate({
            top:-525
        },8000,'linear',function(){
            $('.monitor .content .carousel ul').css('top',0)
        });
    };

    lunbo();
    setInterval(lunbo,8000);

    // 2.3 设备监控模块，鼠标移入移出事件
    $('.monitor .content .carousel ul li').on('mouseenter',function (){
        $(this).addClass('active').siblings().removeClass('active')
    })

    $('.monitor .content .carousel ul li').on('mouseleave',function (){
        $(this).removeClass('active')
    })

    //3. 订单模块（3.1）tab栏切换的效果


})


//入口函数-寿命预测
$(function(){
    var myColor=["#1089E7","#F57474","#56D0E3","#F8B448","#8B78F6"];
    //1.实例化对象
    var myChart = echarts.init(document.querySelector(".realtime .echarts .bar"));
    //2.指定配置和数据
    var option = {

        grid: {
            top: "10%",
            left: '22%',
            bottom: '10%',
            containLabel: false
        },
        // 不显示x轴的信息
        xAxis: {
            // type: 'value',
            // boundaryGap: [0, 0.01]
            show: false
        },
        yAxis:[
            {
                type: 'category',
                data: ['冷凝风机', '通风机', '压缩机', '变频器', '逆变器'],
                // 不显示线
                axisLine: {
                    show: false,
                },
                //不显示刻度
                axisTick:{
                    show: false
                },
                axisLabel:{
                    color:"#fff"
                }  
    
            },
            {
               
                data: ['702', '350', '610', '793', '664'],
                // 不显示线
                axisLine: {
                    show: false,
                },
                //不显示刻度
                axisTick:{
                    show: false
                },
                axisLabel:{
                    color:"#fff"
                }  
    
            },
        ],
        series: [
            {
                name: '条',
                type: 'bar',
                data: [45,34,47,78,69],
                yAxisIndex:0,
                itemStyle:{
                    barBorderRadius:20,
                    color:function(params){
                        return myColor[params.dataIndex];
                    }
                },
                // 柱子之间的距离
                barCategoryGap:50,
                // 柱子的宽度
                barWidth:10,
                // 显示柱子内的文字
                label:{
                    show:true,
                    position:"inside",
                    //{c}会自动的解析为数据  data里面的数据
                    formatter:"{c}%"
                }
            },
            {
                name: '框',
                type: 'bar',
                barCategoryGap:50,
                barWidth:15,
                yAxisIndex:1,
                data: [100,100,100,100,100],
                itemStyle:{
                    color:"none",
                    borderColor:"#00c1de",
                    boderWidth:3,
                    barBorderRadius:15
                }
            }
        ]
    };

    //3.把配置给实例对象
    myChart.setOption(option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function() {
        myChart.resize();
    }); 
})

// 入口函数-健康评估图
$(function(){

    $('.health_assess .head a').on('click',function(){
        // 当前点击的页签添加active类，其他的兄弟页签移除这个类
        $(this).addClass('active').siblings().removeClass('active')
    })
    // 1实例化对象
    var myChart = echarts.init(document.querySelector(".health_assess .echarts .board"));
    
    var dataArr = [{
        value: 85,
        name: '综合健康评分'
    }];
    var color = new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
            offset: 0,
            color: '#5CF9FE' // 0% 处的颜色
        },
        {
            offset: 0.17,
            color: '#468EFD' // 100% 处的颜色
        },
        {
            offset: 0.9,
            color: '#468EFD' // 100% 处的颜色
        },
        {
            offset: 1,
            color: '#5CF9FE' // 100% 处的颜色
        }
    ]);
    var colorSet = [
        [0.91, color],
        [1, '#15337C']
    ];
    var rich = {
        white: {
            fontSize: 20,
            color: '#fff',
            fontWeight: '100',
            padding: [-150, 0, 0, 0]
        },
        bule: {
            fontSize: 50,
            fontFamily: 'DINBold',
            color: '#fff',
            fontWeight: '700',
            padding: [-120, 0, 0, 0],
        },
        radius: {
            width: 350,
            height: 80,
            // lineHeight:80,
            borderWidth: 1,
            borderColor: '#0092F2',
            fontSize: 50,
            color: '#fff',
            backgroundColor: '#1B215B',
            borderRadius: 20,
            textAlign: 'center',
        },
        size: {
            height: 400,
            padding: [100, 0, 0, 0]
        }
    }
    var option = {
        backgroundColor: '#0E1327',
        tooltip: {
            formatter: "{a} <br/>{b} : {c}%"
        },
    
        series: [{ //内圆
                type: 'pie',
                radius: '85%',
                center: ['50%', '50%'],
                z: 0,
                itemStyle: {
                    normal: {
                        color: new echarts.graphic.RadialGradient(.5, .5, 1, [{
                                offset: 0,
                                color: 'rgba(17,24,43,0)'
                            },
                            {
                                offset: .5,
                                // color: '#1E2B57'
                                color:'rgba(28,42,91,.6)'
                            },
                            {
                                offset: 1,
                                color: '#141C33',
                                // color:'rgba(17,24,43,0)'
                            }
                        ], false),
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    },
                },
                hoverAnimation: false,
                label: {
                    show: false,
                },
                tooltip: {
                    show: false
                },
                data: [100],
            },
            {
                type: 'gauge',
                name: '外层辅助',
                radius: '74%',
                startAngle: '225',
                endAngle: '-45',
                splitNumber: '100',
                pointer: {
                    show: false
                },
                detail: {
                    show: false,
                },
                data: [{
                    value: 1
                }],
                // data: [{value: 1, name: 90}],
                title: {
                    show: true,
                    offsetCenter: [0, 30],
                    textStyle: {
                        color: '#fff',
                        fontStyle: 'normal',
                        fontWeight: 'normal',
                        fontFamily: '微软雅黑',
                        fontSize: 20,
                    }
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: [
                            [1, '#00FFFF']
                        ],
                        width: 2,
                        opacity: 1
                    }
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: true,
                    length: 20,
                    lineStyle: {
                        color: '#051932',
                        width: 0,
                        type: 'solid',
                    },
                },
                axisLabel: {
                    show: false
                }
            },
            {
                type: 'gauge',
                radius: '70%',
                startAngle: '225',
                endAngle: '-45',
                pointer: {
                    show: false
                },
                detail: {
                    formatter: function(value) {
                        var num = Math.round(value);
                        return '{bule|' + num + '}{white|分}' + '{size|' + '}\n{radius|综合健康评分}';
                    },
                    rich: rich,
                    "offsetCenter": ['0%', "0%"],
                },
                data: dataArr,
                title: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: colorSet,
                        width: 25,
                        // shadowBlur: 15,
                        // shadowColor: '#B0C4DE',
                        shadowOffsetX: 0,
                        shadowOffsetY: 0,
                        opacity: 1
                    }
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false,
                    length: 25,
                    lineStyle: {
                        color: '#00377a',
                        width: 2,
                        type: 'solid',
                    },
                },
                axisLabel: {
                    show: false
                },
            },
            {
                name: '灰色内圈', //刻度背景
                type: 'gauge',
                z: 2,
                radius: '60%',
                startAngle: '225',
                endAngle: '-45',
                //center: ["50%", "75%"], //整体的位置设置
                axisLine: { // 坐标轴线
                    lineStyle: { // 属性lineStyle控制线条样式
                        color: [
                            [1, '#018DFF']
                        ],
                        width: 2,
                        opacity: 1, //刻度背景宽度
                    }
                },
                splitLine: {
                    show: false
                },
                // data: [{
                //     show: false,
                //     value: '80'
                // }], //作用不清楚
                axisLabel: {
                    show: false
                },
                pointer: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                detail: {
                    show: 0
                }
            },
            {
                name: "白色圈刻度",
                type: "gauge",
                radius: "60%",
                startAngle: 225, //刻度起始
                endAngle: -45, //刻度结束
                z: 4,
                axisTick: {
                    show: false
                },
                splitLine: {
                    length: 16, //刻度节点线长度
                    lineStyle: {
                        width: 2,
                        color: 'rgba(1,244,255, 0.9)'
                    } //刻度节点线
                },
                axisLabel: {
                    color: 'rgba(255,255,255,0)',
                    fontSize: 12,
                }, //刻度节点文字颜色
                pointer: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        opacity: 0
                    }
                },
                detail: {
                    show: false
                },
                data: [{
                    value: 0,
                    name: ""
                }]
            },
            { //内圆
                type: 'pie',
                radius: '56%',
                center: ['50%', '50%'],
                z: 1,
                itemStyle: {
                    normal: {
                        color: new echarts.graphic.RadialGradient(.5, .5, .8, [{
                                offset: 0,
                                color: '#4978EC'
                            },
                            {
                                offset: .5,
                                color: '#1E2B57'
                            },
                            {
                                offset: 1,
                                color: '#141F3D'
                            }
                        ], false),
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    },
                },
                hoverAnimation: false,
                label: {
                    show: false,
                },
                tooltip: {
                    show: false
                },
                data: [100],
            },
        ]
    };


    // 3. 把配置项给实例对象
    myChart.setOption(option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function() {
        myChart.resize();
    });

})


//入口函数-线路图
// $(function(){
//      // 1实例化对象
//      var myChart = echarts.init(document.querySelector(".subway-line .echarts .sublines"));
    
//      var data = [
     
        
//         {
//             name: "沣东自贸园",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [180, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "后卫寨",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [230, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "三桥",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [280, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "皂河",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [330, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "枣园",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [380, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "汉城路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [430, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "开远门",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [480, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "劳动路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [530, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "玉祥门",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [580, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "洒金桥",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [630, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "北大街",
//             symbol: 'circle',
//             symbolSize: [20, 20],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [680, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 1, 1, 0, [{
//                             offset: 0,
//                             color: "#FF1493"
//                         },
//                         {
//                             offset: 1,
//                             color: "#0000FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "五路口",
//             symbol: 'circle',
//             symbolSize: [20, 20],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [730, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 1, 1, 0, [{
//                             offset: 0,
//                             color: "#FF1493"
//                         },
//                         {
//                             offset: 1,
//                             color: "#0000FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "朝阳门",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [780, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "康复路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [830, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "通化门",
//             symbol: 'circle',
//             symbolSize: [20, 20],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [880, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 1, 1, 0, [{
//                             offset: 0,
//                             color: "#FF1493"
//                         },
//                         {
//                             offset: 1,
//                             color: "#0000FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "万寿路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [930, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "长乐坡",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [980, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "浐河",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [1030, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "半坡",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [1080, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "纺织城",
//             symbol: 'circle',
//             symbolSize: [25, 25],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [1130, 600],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#157eff"
//                         },
//                         {
//                             offset: 1,
//                             color: "#35c2ff"
//                         }
//                     ])
//                 }
//             }
//         },
//         //地铁二号线，垂直线路，站点间X轴坐标相同，Y轴坐标相差50
//         {
//             name: "钟楼",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 540],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "永宁门",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 500],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "南稍门",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 450],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "体育场",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 400],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "小寨",
//             symbol: 'circle',
//             symbolSize: [20, 20],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 350],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 1, 1, 0, [{
//                             offset: 0,
//                             color: "#FF1493"
//                         },
//                         {
//                             offset: 1,
//                             color: "#0000FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "纬一街",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 300],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "会展中心",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 250],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "三爻",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 200],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "凤栖原",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 150],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "航天城",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 100],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "韦曲南",
//             symbol: 'circle',
//             symbolSize: [25, 25],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 50],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "安远门",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 660],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "龙首原",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 700],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "大明宫西",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 750],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "市图书馆",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 800],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "凤城五路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 850],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "行政中心",
//             symbol: 'circle',
//             symbolSize: [20, 20],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 900],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 1, 1, 0, [{
//                             offset: 0,
//                             color: "#FF1493"
//                         },
//                         {
//                             offset: 1,
//                             color: "#0000FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "运动公园",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 950],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "北苑",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 1000],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "北客站",
//             symbol: 'circle',
//             symbolSize: [25, 25],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [680, 1050],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "red"
//                         },
//                         {
//                             offset: 1,
//                             color: "red"
//                         }
//                     ])
//                 }
//             }
//         },
//         //地铁三号线
//         {
//             name: "吉祥村",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [580, 350],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "太白南路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [520, 350],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "科技路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'top',
//             },
//             value: [460, 350],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "延平门",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [400, 350],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
      
//         {
//             name: "桃花潭",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [1000, 757],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "浐灞中心",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [1040, 780],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "香湖湾",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [1040, 830],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "务庄",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [1040, 880],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "国际港务区",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [1040, 930],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "双寨",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [1040, 980],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "新筑",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [1040, 1030],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "保税区",
//             symbol: 'circle',
//             symbolSize: [25, 25],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [1040, 1080],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#FF00FF"
//                         },
//                         {
//                             offset: 1,
//                             color: "#FF00FF"
//                         }
//                     ])
//                 }
//             }
//         },
//         //地铁四号线
      
       
//         {
//             name: "百花村",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [730, 835],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#48D1CC"
//                         },
//                         {
//                             offset: 1,
//                             color: "#48D1CC"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "常青路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [730, 865],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#48D1CC"
//                         },
//                         {
//                             offset: 1,
//                             color: "#48D1CC"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "市中医院",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [710, 890],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#48D1CC"
//                         },
//                         {
//                             offset: 1,
//                             color: "#48D1CC"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "文景路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [550, 900],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#48D1CC"
//                         },
//                         {
//                             offset: 1,
//                             color: "#48D1CC"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "凤城九路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [530, 930],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#48D1CC"
//                         },
//                         {
//                             offset: 1,
//                             color: "#48D1CC"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "凤城十二路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [530, 970],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#48D1CC"
//                         },
//                         {
//                             offset: 1,
//                             color: "#48D1CC"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "元朔路",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [530, 1010],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#48D1CC"
//                         },
//                         {
//                             offset: 1,
//                             color: "#48D1CC"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "北客站(北广场)",
//             symbol: 'circle',
//             symbolSize: [25, 25],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [640, 1100],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#48D1CC"
//                         },
//                         {
//                             offset: 1,
//                             color: "#48D1CC"
//                         }
//                     ])
//                 }
//             }
//         },
//         //机场城际
//         {
//             name: "渭河南",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [530, 1120],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "秦宫",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'left',
//             },
//             value: [450, 1145],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "秦汉新城",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [380, 1105],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "长陵",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [310, 1080],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "摆旗寨",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [230, 1070],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "艺术中心",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [170, 1100],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "空港新城",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [120, 1150],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "机场（T5）",
//             symbol: 'circle',
//             symbolSize: [15, 15],
//             label: {
//                 color: "#efefef",
//                 position: 'right',
//             },
//             value: [80, 1190],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//         {
//             name: "机场西（T1、T2、T3）",
//             symbol: 'circle',
//             symbolSize: [25, 25],
//             label: {
//                 color: "#efefef",
//                 position: 'bottom',
//             },
//             value: [20, 1130],
//             x: 1000,
//             y: 1000,
//             fixed: true,
//             category: 2,
//             itemStyle: {
//                 normal: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
//                             offset: 0,
//                             color: "#20B2AA"
//                         },
//                         {
//                             offset: 1,
//                             color: "#20B2AA"
//                         }
//                     ])
//                 }
//             }
//         },
//     ];
   
//    var option = ({
//          title: {
//             text: '西安地铁线路图',
//             textStyle: {
//                 color: 'white',
//                 fontSize: 20
//             },
//             x: 'center',
//             top: 10
//          },
//         //不设置背景颜色就是透明色
//          backgroundColor: '#000',
//          xAxis: {
//             show: false,
//             min: 0,
//             max: 1200,
//             // type: "value",
//             //开启x轴坐标
//               axisPointer: {
//                   show: true
//               },
//         },
//         yAxis: {
//             show: false,
//             min: 0,
//             max: 1200,
//             //   type: "value",
//             //开启y轴坐标
//               axisPointer: {
//                   show: true
//               },
//         },
//         tooltip: {},
//         //  legend: {
//         //     show: false
//         //  },
//         series: [{
//             type: "graph",
//             zlevel: 5,
//             draggable: false,
//             coordinateSystem: "cartesian2d", //使用二维的直角坐标系（也称笛卡尔坐标系）
   
//             // edgeSymbolSize: [0, 8], //边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定
//             // edgeLabel: {
//             //   normal: {
//             //     textStyle: {
//             //       fontSize: 60
//             //     }
//             //   }
//             // },
//             symbol: "rect",
//             symbolOffset: ["15%", 0],
   
//             label: {
//                 normal: {
//                     show: true
//                 }
//             },
//             data: data,
//             links: [{
//                     source: "沣河森林公园",
//                     target: "北槐"
//                     // lineStyle: {
//                     //   normal: {
//                     //     color: "#12b5d0",
//                     //
//                     //   }
//                     // }
//                 },
//                 {
//                     source: "北槐",
//                     target: "上林路",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "上林路",
//                     target: "沣东自贸园",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "沣东自贸园",
//                     target: "后卫寨",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
   
//                 {
//                     source: "后卫寨",
//                     target: "三桥",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
   
//                 {
//                     source: "三桥",
//                     target: "皂河",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
   
//                 {
//                     source: "皂河",
//                     target: "枣园"
//                     // lineStyle: {
//                     //   normal: {
//                     //     color: "#12b5d0",
//                     //
//                     //   }
//                     // }
//                 },
//                 {
//                     source: "枣园",
//                     target: "汉城路",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "汉城路",
//                     target: "开远门",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "开远门",
//                     target: "劳动路",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "劳动路",
//                     target: "玉祥门",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "玉祥门",
//                     target: "洒金桥",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "洒金桥",
//                     target: "北大街",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "北大街",
//                     target: "五路口",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "五路口",
//                     target: "朝阳门",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "朝阳门",
//                     target: "康复路",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "康复路",
//                     target: "通化门",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "通化门",
//                     target: "万寿路",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "万寿路",
//                     target: "长乐坡",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "长乐坡",
//                     target: "浐河",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "浐河",
//                     target: "半坡",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 {
//                     source: "半坡",
//                     target: "纺织城",
//                     lineStyle: {
//                         normal: {
//                             // color: "#12b5d0",
//                         }
//                     }
//                 },
//                 //地铁二号线连接
                
//                 {
//                     source: "北大街",
//                     target: "安远门",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "安远门",
//                     target: "龙首原",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "龙首原",
//                     target: "大明宫西",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "大明宫西",
//                     target: "市图书馆",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "市图书馆",
//                     target: "凤城五路",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "凤城五路",
//                     target: "行政中心",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "行政中心",
//                     target: "运动公园",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "运动公园",
//                     target: "北苑",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "北苑",
//                     target: "北客站",
//                     lineStyle: {
//                         normal: {
//                             color: "red",
//                         }
//                     }
//                 },
//                 {
//                     source: "鱼化寨",
//                     target: "丈八北路",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "丈八北路",
//                     target: "延平门",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "延平门",
//                     target: "科技路",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "科技路",
//                     target: "太白南路",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "太白南路",
//                     target: "吉祥村",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "吉祥村",
//                     target: "小寨",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "小寨",
//                     target: "大雁塔",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "大雁塔",
//                     target: "北池头",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "北池头",
//                     target: "青龙寺",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "青龙寺",
//                     target: "延兴门",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "延兴门",
//                     target: "咸宁路",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "咸宁路",
//                     target: "长乐公园",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "长乐公园",
//                     target: "通化门",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "通化门",
//                     target: "胡家庙",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "胡家庙",
//                     target: "石家街",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "石家街",
//                     target: "辛家庙",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "辛家庙",
//                     target: "广泰门",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "广泰门",
//                     target: "桃花潭",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "桃花潭",
//                     target: "浐灞中心",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "浐灞中心",
//                     target: "香湖湾",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "香湖湾",
//                     target: "务庄",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "务庄",
//                     target: "国际港务区",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "国际港务区",
//                     target: "双寨",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "双寨",
//                     target: "新筑",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 {
//                     source: "新筑",
//                     target: "保税区",
//                     lineStyle: {
//                         normal: {
//                             color: "#FF00FF",
//                         }
//                     }
//                 },
//                 //地铁四号线和机场城际的连线
//                 {
//                     source: "航天新城",
//                     target: "航天东路",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "航天东路",
//                     target: "神舟大道",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "神舟大道",
//                     target: "东长安街",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "东长安街",
//                     target: "飞天路",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "飞天路",
//                     target: "航天大道",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "航天大道",
//                     target: "金滹沱",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "金滹沱",
//                     target: "曲江池西",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "曲江池西",
//                     target: "大唐芙蓉园",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "大唐芙蓉园",
//                     target: "大雁塔",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "大雁塔",
//                     target: "西安科技大学",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "西安科技大学",
//                     target: "建筑科技大学",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "建筑科技大学",
//                     target: "和平门",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "和平门",
//                     target: "大差市",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "大差市",
//                     target: "五路口",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "五路口",
//                     target: "火车站",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "火车站",
//                     target: "含元殿",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "含元殿",
//                     target: "大明宫",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "大明宫",
//                     target: "大明宫北",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "大明宫北",
//                     target: "余家寨",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "余家寨",
//                     target: "百花村",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "百花村",
//                     target: "常青路",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "常青路",
//                     target: "市中医院",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "市中医院",
//                     target: "行政中心",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "行政中心",
//                     target: "文景路",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "文景路",
//                     target: "凤城九路",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "凤城九路",
//                     target: "凤城十二路",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "凤城十二路",
//                     target: "元朔路",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "元朔路",
//                     target: "北客站(北广场)",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 //机场城际各站点连线
//                 {
//                     source: "北客站(北广场)",
//                     target: "渭河南",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "渭河南",
//                     target: "秦宫",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "秦宫",
//                     target: "秦汉新城",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "秦汉新城",
//                     target: "长陵",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "长陵",
//                     target: "摆旗寨",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "摆旗寨",
//                     target: "艺术中心",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "艺术中心",
//                     target: "空港新城",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "空港新城",
//                     target: "机场（T5）",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//                 {
//                     source: "机场（T5）",
//                     target: "机场西（T1、T2、T3）",
//                     lineStyle: {
//                         normal: {
//                             color: "#48D1CC",
//                         }
//                     }
//                 },
//             ],
//             lineStyle: {
//                 normal: {
//                     opacity: 0.6, //线条透明度
//                     color: "#53B5EA",
//                     curveness: 0, //站点间连线曲度，0表示直线
//                     width: 10 //线条宽度
//                 }
//             }
//         }, 
//         {
//                type: "lines",
//                coordinateSystem: "cartesian2d",
//                z: 1,
//                zlevel:7,
//                animation: true,
//                effect: {
//                  show: true,
//                  period: 5,
//                  trailLength: 0.71,
//                  symbolSize: 14,
//                  symbol: "circle",
//                  loop: true,
//                  color: 'yellow'
//                //   color: "rgba(55,155,255,0.5)"
//                },
//                lineStyle: {
//                  normal: {
//                    // color: "green",
//                    width: 0,
//                    curveness: 0  //动画线路的曲度
//                  }
//                },
   
//                data: [
//                  {  //一号线
//                    coords: [
//                      [5, 600],
//                      [1130, 600]
//                    ]
//                  },
//                  {  //二号线
//                    coords: [
//                      [680, 50],
//                      [680, 1050]
//                    ]
//                  },
//                //   {  //三号线
//                //     coords: [
//                //       [280, 350],
//                //       [1040, 1080]
//                //     ]
//                //   }
//                ]
//              },
        
//         ]
//    });
 
//      // 3. 把配置项给实例对象
//      myChart.setOption(option);
//      // 4. 让图表跟随屏幕自动的去适应
//      window.addEventListener("resize", function() {
//          myChart.resize();
//      });
 
// })





