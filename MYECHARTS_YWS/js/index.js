(function() {
    // 1实例化对象
    var myChart = echarts.init(document.querySelector(".bar .chart"));
    // 2. 指定配置项和数据
    var option = {
        color: ["#2f89cf"],
        tooltip: {
            trigger: "axis",
            axisPointer: {
                // 坐标轴指示器，坐标轴触发有效
                type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        // 修改图表的大小
        grid: {
            left: "0%",
            top: "10px",
            right: "0%",
            bottom: "4%",
            containLabel: true
        },
        xAxis: [{
            type: "category",
            data: [
                "旅游行业",
                "教育培训",
                "游戏行业",
                "医疗行业",
                "电商行业",
                "社交行业",
                "金融行业"
            ],
            axisTick: {
                alignWithLabel: true
            },
            // 修改刻度标签 相关样式
            axisLabel: {
                color: "rgba(255,255,255,.6) ",
                fontSize: "12"
            },
            // 不显示x坐标轴的样式
            axisLine: {
                show: false
            }
        }],
        yAxis: [{
            type: "value",
            // 修改刻度标签 相关样式
            axisLabel: {
                color: "rgba(255,255,255,.6) ",
                fontSize: 12
            },
            // y轴的线条改为了 2像素
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)",
                    width: 2
                }
            },
            // y轴分割线的颜色
            splitLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)"
                }
            }
        }],
        series: [{
            name: "直接访问",
            type: "bar",
            barWidth: "35%",
            data: [200, 300, 300, 900, 1500, 1200, 600],
            itemStyle: {
                // 修改柱子圆角
                barBorderRadius: 5
            }
        }]
    };
    // 3. 把配置项给实例对象
    myChart.setOption(option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function() {
        myChart.resize();
    });
})();

//柱状图2
(function() {
    //1.实例化对象
    var myChart = echarts.init(document.querySelector(".bar2 .chart"));
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
        yAxis: {
            type: 'category',
            data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)'],
            // 不显示线
            axisLine: {
                show: false,
            },
            // 不显示刻度
            axisTick: {
                show: false,
            },
            // 把刻度标签里面的文字颜色设置为白色
            axisLabel: {
                color: "rgba(255,255,255,10)"
            }

        },
        series: [{
                name: '条',
                // 柱子的间距
                barCategoryGap: 50,
                //柱子的宽
                barWidth: 10,
                // 柱子的圆角
                itemStyle: {
                    noraml: {
                        barBorderRadius: 20,
                    }
                },
                type: 'bar',
                data: [18203, 23489, 29034, 104970, 131744, 630230]
            },
            {
                name: '2012年',
                type: 'bar',
                data: [19325, 23438, 31000, 121594, 134141, 681807]
            }
        ]
    };

    //3.把配置给实例对象
    myChart.setOption(option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function() {
        myChart.resize();
    });

})()