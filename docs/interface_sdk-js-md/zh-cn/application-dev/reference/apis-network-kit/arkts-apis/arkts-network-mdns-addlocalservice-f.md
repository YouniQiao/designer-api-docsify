# addLocalService

## 导入模块

```TypeScript
import { mdns } from 'kits/@kit.NetworkKit';
```

## addLocalService

```TypeScript
function addLocalService(context: Context, serviceInfo: LocalServiceInfo,
    callback: AsyncCallback<LocalServiceInfo>): void
```

Adds an mDNS service.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-mdns-function addLocalService(context: Context, serviceInfo: LocalServiceInfo,    callback: AsyncCallback<LocalServiceInfo>): void--><!--Device-mdns-function addLocalService(context: Context, serviceInfo: LocalServiceInfo,    callback: AsyncCallback<LocalServiceInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Indicates the context of application or capability. |
| serviceInfo | [LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md) | 是 | Information about the mDNS service. {@link LocalServiceInfo} |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;LocalServiceInfo&gt; | 是 | the callback of addLocalService. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2204003 | Callback duplicated. |
| 2100003 | System internal error. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

## 示例

Stage模型示例：

```TypeScript
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.addLocalService(context, localServiceInfo, (error:BusinessError, data:mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```


## addLocalService

```TypeScript
function addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>
```

Adds an mDNS service.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-mdns-function addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>--><!--Device-mdns-function addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Indicates the context of application or capability. |
| serviceInfo | [LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md) | 是 | Information about the mDNS service. {@link LocalServiceInfo} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;LocalServiceInfo&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2204003 | Callback duplicated. |
| 2100003 | System internal error. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

## 示例

Stage模型示例：

```TypeScript
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
    address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.addLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

