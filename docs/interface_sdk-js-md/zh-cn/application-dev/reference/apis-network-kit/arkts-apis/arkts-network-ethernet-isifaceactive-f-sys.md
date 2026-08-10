# isIfaceActive（系统接口）

## 导入模块

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## isIfaceActive

```TypeScript
function isIfaceActive(iface: string, callback: AsyncCallback<number>): void
```

Check whether the specified network is active.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function isIfaceActive(iface: string, callback: AsyncCallback<number>): void--><!--Device-ethernet-function isIfaceActive(iface: string, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iface | string | 是 | Indicates the network interface name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 | the callback of isIfaceActive. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 2201005 | Device information does not exist. |

## 示例

```TypeScript
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.isIfaceActive("eth0", (error: BusinessError, value: number) => {
  if (error) {
    console.error("whether2Activate callback error = " + JSON.stringify(error));
  } else {
    console.info("whether2Activate callback = " + JSON.stringify(value));
  }
});
```


## isIfaceActive

```TypeScript
function isIfaceActive(iface: string): Promise<number>
```

Check whether the specified network is active.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function isIfaceActive(iface: string): Promise<number>--><!--Device-ethernet-function isIfaceActive(iface: string): Promise<number>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iface | string | 是 | Indicates the network interface name. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | the promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 2201005 | Device information does not exist. |

## 示例

```TypeScript
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.isIfaceActive("eth0").then((data: number) => {
  console.info("isIfaceActive promise = " + JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.error("isIfaceActive promise error = " + JSON.stringify(error));
});
```

