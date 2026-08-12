# getOAID

## getOAID

```TypeScript
function getOAID(callback: AsyncCallback<string>): void
```

获取开放匿名设备标识符（OAID）。使用callback异步回调。

> **说明：**
> 
> 设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**起始版本：** 10

**需要权限：** ohos.permission.APP_TRACKING_CONSENT

<!--Device-identifier-function getOAID(callback: AsyncCallback<string>): void--><!--Device-identifier-function getOAID(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Advertising.OAID

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300001-系统内部错误) |

## 示例

```TypeScript
import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';

identifier.getOAID((err: BusinessError, data: string) => {
  if (err.code) {
    return;
  }
  const oaid: string = data;
  hilog.info(0x0000, 'testTag', `Succeeded in getting OAID: ${oaid}`);
});
```


## getOAID

```TypeScript
function getOAID(): Promise<string>
```

获取开放匿名设备标识符（OAID）。使用Promise异步回调。

> **说明：**
> 
> 设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**起始版本：** 10

**需要权限：** ohos.permission.APP_TRACKING_CONSENT

<!--Device-identifier-function getOAID(): Promise<string>--><!--Device-identifier-function getOAID(): Promise<string>-End-->

**系统能力：** SystemCapability.Advertising.OAID

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300001-系统内部错误) |

## 示例

```TypeScript
import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

void identifier.getOAID().then((data: string) => {
  const oaid: string = data;
  hilog.info(0x0000, 'testTag', `Succeeded in getting OAID: ${oaid}`);
}).catch((error: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to get oaid. Code is ${error.code}, message is ${error.message}`);
});
```
