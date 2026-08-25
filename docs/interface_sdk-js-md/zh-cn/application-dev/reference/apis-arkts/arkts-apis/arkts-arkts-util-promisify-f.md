# promisify

## 导入模块

```TypeScript
import { util } from '@kit.ArkTS';
```

## promisify

```TypeScript
function promisify(original: (err: Object, value: Object) => void): Function
```

接收一个采用"错误优先"回调模式的函数，即以`(err, value) =&gt; callback`作为最后一个参数，并返回其Promise函数。 适用于将旧版回调式异步API转换为Promise风格，以便使用async/await语法进行调用，从而简化异步代码编写。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| original | (err: Object, value: Object) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| Function |

**示例**

ArkTS-Dyn示例：

```TypeScript
async function fn() {
  return 'hello world';
}
const addCall = util.promisify(util.callbackWrapper(fn));
(async () => {
  try {
    let res: string = await addCall();
    console.info(res);
    // 输出结果：hello world
  } catch (err) {
    console.info(err);
  }
})();
```

ArkTS-Sta示例：

```TypeScript
let func: Function =
  (val: Any, callback: (err: Error | null, ...value: FixedArray<Any>) => void) => {
  callback(null, val);
}
let val = util.promisify(func);
let res = await val(42);
console.info(new String(res)); // 输出结果：42
```
