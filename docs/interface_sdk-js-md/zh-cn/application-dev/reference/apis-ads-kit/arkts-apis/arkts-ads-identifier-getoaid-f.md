# getOAID

## 导入模块

```TypeScript
import { identifier } from 'kits/@kit.AdsKit';
```

## getOAID

```TypeScript
function getOAID(callback: AsyncCallback<string>): void
```

获取开放匿名设备标识符（OAID）。使用callback异步回调。

> **说明：**&gt;
> 设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**起始版本：** 10

**需要权限：** ohos.permission.APP_TRACKING_CONSENT

**系统能力：** SystemCapability.Advertising.OAID

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17300001](../errorcode-oaid.md#17300001-系统内部错误) |


## getOAID

```TypeScript
function getOAID(): Promise<string>
```

获取开放匿名设备标识符（OAID）。使用Promise异步回调。

> **说明：**&gt;
> 设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**起始版本：** 10

**需要权限：** ohos.permission.APP_TRACKING_CONSENT

**系统能力：** SystemCapability.Advertising.OAID

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17300001](../errorcode-oaid.md#17300001-系统内部错误) |
