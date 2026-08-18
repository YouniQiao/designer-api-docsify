# getBundlePriorityConfig（系统接口）

## 导入模块

```TypeScript
```

## getBundlePriorityConfig

```TypeScript
function getBundlePriorityConfig(bundle: BundleOption): Promise<string>
```

获取应用的优先功能配置。

**起始版本：** 23

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getBundlePriorityConfig(bundle: BundleOption): Promise<string>--><!--Device-notificationManager-function getBundlePriorityConfig(bundle: BundleOption): Promise<string>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const bundleOption : notificationManager.BundleOption = { bundle: 'bundleName', uid: 0 };
notificationManager.getBundlePriorityConfig(bundleOption).then((value: string) => {
  hilog.info(0x0000, 'testTag', `getBundlePriorityConfig value is ${value}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `getBundlePriorityConfig failed, code is ${err.code}, message is ${err.message}`);
});
```
