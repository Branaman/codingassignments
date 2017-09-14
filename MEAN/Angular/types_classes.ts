var myNum: number = 5;
var myString: string = "Hello Universe";
var myArr: Array<number>= [1,2,3,4];
var myObj: Object = { name:'Bill'};
var anythingVariable: any = "Hey";
var anythingVariable: any = 25;
var arrayOne:boolean[] = [true, false, true, true];
var arrayTwo: any[] = [1, 'abc', true, 2];
var myObj: Object = { x: 5, y: 10 };
// object constructor
class MyNode {
    val: number;
    _priv: number;
    constructor(val:number) {
        this.val = 0;
        this.val = val;
    }
    doSomething() {
        this._priv = 10;
    };
};
let myNodeInstance = new MyNode(1);
console.log(myNodeInstance.val);
function myFunction(val:string):void {
    console.log(val);
}
function sendingErrors(message:string):void {
	throw new Error(message);
}
