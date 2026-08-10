# setAppNet

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## setAppNet

```TypeScript
function setAppNet(netHandle: NetHandle, callback: AsyncCallback<void>): void
```

Binds a process to {@code NetHandle}.&lt;p&gt;All the sockets created from the process will be bound to the {@code NetHandle},and the resolution of all host names will be managed by the {@code NetHandle}.&lt;/p&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

<!--Device-connection-function setAppNet(netHandle: NetHandle, callback: AsyncCallback<void>): void--><!--Device-connection-function setAppNet(netHandle: NetHandle, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | 是 | Indicates the handle. For details, see {@link NetHandle}. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback of setAppNet. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## 示例

以下示例以绑定WIFI网络为例，结合[on('netAvailable')](#onnetavailable)、[on('netLost')](#onnetlost)接口，当监听到WIFI网络可用时绑定WIFI网络，不可用时解绑，使用默认网络。

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建NetConnection对象。仅关注WIFI网络，需要指定网络类型为WIFI网络。
let netCon = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: [connection.NetBearType.BEARER_WIFI]
  }
});

// 使用on接口订阅网络可用事件
netCon.on('netAvailable', (netHandle: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(netHandle));
  connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to setAppNet, netid: " + JSON.stringify(netHandle.netId));
  });
});

// 使用on接口订阅网络丢失事件。
netCon.on('netLost', (netHandle: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(netHandle));
  // 网络丢失时，需要主动解除指定网络的绑定关系
  netHandle.netId = 0;
  connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to setAppNet, netid: " + JSON.stringify(netHandle.netId));
  });
});

// 注册网络状态变化事件。此接口要在调用on后调用。
netCon.register((error: BusinessError) => {
  if (error) {
    console.error(`Failed to get request.Code:${error.code}, message:${error.message}`);
  }
});
```


## setAppNet

```TypeScript
function setAppNet(netHandle: NetHandle): Promise<void>
```

Binds a process to {@code NetHandle}.&lt;p&gt;All the sockets created from the process will be bound to the {@code NetHandle},and the resolution of all host names will be managed by the {@code NetHandle}.&lt;/p&gt;

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**需要权限：** ohos.permission.INTERNET

<!--Device-connection-function setAppNet(netHandle: NetHandle): Promise<void>--><!--Device-connection-function setAppNet(netHandle: NetHandle): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | 是 | Indicates the handle. For details, see {@link NetHandle}. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## 示例

以下示例以绑定WIFI网络为例，结合[on('netAvailable')](#onnetavailable)、[on('netLost')](#onnetlost)接口，当监听到WIFI网络可用时绑定WIFI网络，不可用时解绑，使用默认网络。

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建NetConnection对象。仅关注WIFI网络，需要指定网络类型为WIFI网络。
let netCon = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: [connection.NetBearType.BEARER_WIFI]
  }
});

// 使用on接口订阅网络可用事件
netCon.on('netAvailable', (netHandle: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(netHandle));
  connection.setAppNet(netHandle).then(() => {
    console.info("Succeeded to setAppNet, netid: " + JSON.stringify(netHandle.netId));
  }).catch((error: BusinessError) => {
    console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
  })
});

// 使用on接口订阅网络丢失事件。
netCon.on('netLost', (netHandle: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(netHandle));
  // 网络丢失时，需要主动解除指定网络的绑定关系
  netHandle.netId = 0;
  connection.setAppNet(netHandle).then(() => {
    console.info("Succeeded to setAppNet, netid: " + JSON.stringify(netHandle.netId));
  }).catch((error: BusinessError) => {
    console.error(`Failed to setAppNet. Code:${error.code}, message:${error.message}`);
  })
});

// 注册网络状态变化事件。此接口要在调用on后调用。
netCon.register((error: BusinessError) => {
  if (error) {
    console.error(`Failed to get request.Code:${error.code}, message:${error.message}`);
  }
});
```

