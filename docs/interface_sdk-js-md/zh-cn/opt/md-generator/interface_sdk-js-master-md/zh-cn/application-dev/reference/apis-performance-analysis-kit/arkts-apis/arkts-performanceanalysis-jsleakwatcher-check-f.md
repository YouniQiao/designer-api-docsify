# check

## check

```TypeScript
function check(): string
```

获取已通过jsLeakWatcher.watch注册发生泄漏的对象列表，触发GC后未被回收的对象会被标记为泄漏。

**起始版本：** 12

<!--Device-jsLeakWatcher-function check(): string--><!--Device-jsLeakWatcher-function check(): string-End-->

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
let leakObjlist:string = jsLeakWatcher.check();
```
