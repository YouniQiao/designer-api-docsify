# watch

## 导入模块

```TypeScript
```

## watch

```TypeScript
function watch(obj: object, msg: string): void
```

注册待检测泄漏的对象。

**起始版本：** 26.1.0

<!--Device-jsLeakWatcher-function watch(obj: object, msg: string): void--><!--Device-jsLeakWatcher-function watch(obj: object, msg: string): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | object | 是 |
| msg | string | 是 |

**示例**

```TypeScript
let obj:Object = new Object();
jsLeakWatcher.watch(obj, "Trace Object");
```
