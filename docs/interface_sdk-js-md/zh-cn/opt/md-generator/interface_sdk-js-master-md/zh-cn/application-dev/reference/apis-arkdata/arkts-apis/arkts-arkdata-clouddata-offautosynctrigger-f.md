# offAutoSyncTrigger

## offAutoSyncTrigger

```TypeScript
function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void
```

取消订阅自动同步触发事件通知。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-cloudData-function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void--><!--Device-cloudData-function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AutoSyncTriggerInfo](arkts-arkdata-clouddata-autosynctriggerinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

```TypeScript
function autoSyncTriggerObserver(info: cloudData.AutoSyncTriggerInfo) {
  console.info(`Auto sync triggered, mode: ${info.mode}`);
}

// 订阅
cloudData.onAutoSyncTrigger(autoSyncTriggerObserver);

// 取消指定订阅
cloudData.offAutoSyncTrigger(autoSyncTriggerObserver);

// 取消所有订阅
cloudData.offAutoSyncTrigger();
```
