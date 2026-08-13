# dump

## dump

```TypeScript
function dump(filePath: string): Array<string>
```

导出泄漏列表和虚拟机内存快照。

**起始版本：** 26.1.0

**废弃版本：** -1

<!--Device-jsLeakWatcher-function dump(filePath: string): Array<string>--><!--Device-jsLeakWatcher-function dump(filePath: string): Array<string>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## 示例

```TypeScript
let context = this.getUIContext().getHostContext();
let files: Array<string> = jsLeakWatcher.dump(context?.filesDir);
```
