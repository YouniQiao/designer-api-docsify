# setCameraTrackingEnabled

## setCameraTrackingEnabled

```TypeScript
function setCameraTrackingEnabled(isEnabled: boolean): void
```

启用或禁用摄像机跟踪

**起始版本：** 20

<!--Device-mechanicManager-function setCameraTrackingEnabled(isEnabled: boolean): void--><!--Device-mechanicManager-function setCameraTrackingEnabled(isEnabled: boolean): void-End-->

**系统能力：** SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [33300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300002-设备未连接) |
| [33300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300003-功能不支持) |

## 示例

```TypeScript
console.info('Enable tracing');
// 调用setCameraTrackingEnabled方法，参数true表示启用摄像头跟踪
mechanicManager.setCameraTrackingEnabled(true);
console.info('Succeeded in enabling tracking.');
```
