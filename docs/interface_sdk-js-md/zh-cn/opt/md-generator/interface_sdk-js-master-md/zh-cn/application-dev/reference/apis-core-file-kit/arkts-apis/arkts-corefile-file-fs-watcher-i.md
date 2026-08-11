# Watcher

文件目录变化监听对象。由createWatcher接口获得。

**起始版本：** 10

<!--Device-unnamed-export interface Watcher--><!--Device-unnamed-export interface Watcher-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## start

```TypeScript
start(): void
```

开启监听。

**起始版本：** 10

<!--Device-Watcher-start(): void--><!--Device-Watcher-start(): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900005 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900042 |
| 13900011 |

## 示例

```TypeScript
let filePath = pathDir + "/test.txt";
let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```

## stop

```TypeScript
stop(): void
```

停止监听并移除Watcher对象。

**起始版本：** 10

<!--Device-Watcher-stop(): void--><!--Device-Watcher-stop(): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900005 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900042 |
| 13900011 |

## 示例

```TypeScript
let filePath = pathDir + "/test.txt";
let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```
