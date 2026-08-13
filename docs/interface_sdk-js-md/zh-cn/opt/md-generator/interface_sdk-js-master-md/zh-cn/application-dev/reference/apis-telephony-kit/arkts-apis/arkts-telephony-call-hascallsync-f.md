# hasCallSync

## hasCallSync

```TypeScript
function hasCallSync(): boolean
```

判断是否存在通话。

**起始版本：** 10

<!--Device-call-function hasCallSync(): boolean--><!--Device-call-function hasCallSync(): boolean-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let hasCall: boolean = call.hasCallSync();
console.info(`hasCallSync success, has call is ` + hasCall);
```
