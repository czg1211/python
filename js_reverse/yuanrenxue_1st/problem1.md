1.从翻页接口的请求堆栈中找到request；
2.解原js的ob混淆，得到problem1_1.js;
3.分析可知m的值与window["f"]相关，在浏览器控制台输入以下脚本即可hook到设置window.f所在位置：
    Object.defineProperty(window, 'f', {
       set: function(val) {
                console.log('f的值:', val);
                debugger
                return val;
            }
        }
    )
4.将window.f所在位置的js文件复制下来，得到problem1.js文件；
5.分析可知window.f的值为调用hex_md5方法传入时间戳的字符串格式，结合problem1_1.js中相关逻辑，编写以下函数供python调用即可
function run() {
    var date = Date.parse(new Date()) + (16798545 + -72936737 + 156138192);
    window.f = hex_md5(date.toString());
    var result =  window.f + "丨" + date / 1000;
    return result
}