# Watcher

Watcher是文件变化监听的实例，调用Watcher.stop()方法（同步或异步）来停止文件监听。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [Watcher](arkts-corefile-file-fs-watcher-i.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
```

## stop

```TypeScript
stop(): Promise<void>
```

关闭watcher监听，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [stop](arkts-corefile-file-fs-watcher-i.md#stop)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

关闭watcher监听，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [stop](arkts-corefile-file-fs-watcher-i.md#stop)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
