# AVSession

调用[avSession.createAVSession](arkts-avsession-avsession-createavsession-f.md)后，返回会话的实例，可以获得会话ID，完成设置元数据，播放状态信息等操作。

> **说明：**&gt;
> - 本Interface首批接口从API version 10开始支持。

**起始版本：** 23

<!--Device-avSession-interface AVSession--><!--Device-avSession-interface AVSession-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

## 导入模块

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## activate

```TypeScript
activate(callback: AsyncCallback<void>): void
```

激活会话，激活后可正常使用会话。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-activate(callback: AsyncCallback<void>): void--><!--Device-AVSession-activate(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当会话激活成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.activate().then(() => {
  console.info('Succeeded in activating.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.activate((err: BusinessError) => {
  if (err) {
    console.error(`Failed to activate, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in activating.');
});
```

## activate

```TypeScript
activate(): Promise<void>
```

激活会话，激活后可正常使用会话。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-activate(): Promise<void>--><!--Device-AVSession-activate(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当会话激活成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [activate](#activate)

## deactivate

```TypeScript
deactivate(callback: AsyncCallback<void>): void
```

禁用当前会话。结果通过callback异步回调方式返回。禁用当前会话的功能，可通过[activate](#activate)恢复。

**起始版本：** 23

<!--Device-AVSession-deactivate(callback: AsyncCallback<void>): void--><!--Device-AVSession-deactivate(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当禁用会话成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.deactivate().then(() => {
  console.info('Deactivate : SUCCESS ');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.deactivate((err: BusinessError) => {
  if (err) {
    console.error(`Failed to deactivate, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in deactivating.');
});
```

## deactivate

```TypeScript
deactivate(): Promise<void>
```

禁用当前会话的功能，可通过[activate](#activate)恢复。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-deactivate(): Promise<void>--><!--Device-AVSession-deactivate(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当禁用会话成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [deactivate](#deactivate)

## destroy

```TypeScript
destroy(callback: AsyncCallback<void>): void
```

销毁当前会话，使当前会话完全失效。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-destroy(callback: AsyncCallback<void>): void--><!--Device-AVSession-destroy(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当会话销毁成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.destroy().then(() => {
  console.info('Succeeded in destroying.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.destroy((err: BusinessError) => {
  if (err) {
    console.error(`Failed to destroy, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in destroying.');
});
```

```TypeScript
avcontroller.destroy().then(() => {
  console.info('Succeeded in destroying.');
});
```

```TypeScript
avcontroller.destroy((err: BusinessError) => {
  if (err) {
    console.error(`Failed to destroy controller, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in destroying.');
});
```

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁当前会话，使当前会话完全失效。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-destroy(): Promise<void>--><!--Device-AVSession-destroy(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当会话销毁成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [destroy](#destroy)

## dispatchSessionEvent

```TypeScript
dispatchSessionEvent(event: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void
```

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。使用callback异步回调。

**起始版本：** 10

<!--Device-AVSession-dispatchSessionEvent(event: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void--><!--Device-AVSession-dispatchSessionEvent(event: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 需要设置的会话事件的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的会话事件内容。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当会话事件设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
let eventName = "dynamic_lyric";
currentAVSession.dispatchSessionEvent(eventName, {lyric : "This is lyric"}).then(() => {
  console.info('Succeeded in dispatching session event.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let eventName: string = "dynamic_lyric";
currentAVSession.dispatchSessionEvent(eventName, {lyric : "This is lyric"}, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to dispatch session event, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in dispatching session event.');
});
```

## dispatchSessionEvent

```TypeScript
dispatchSessionEvent(event: string, args: Record<string, Object>, callback: AsyncCallback<void>): void
```

Dispatch the session event of this session.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-dispatchSessionEvent(event: string, args: Record<string, Object>, callback: AsyncCallback<void>): void--><!--Device-AVSession-dispatchSessionEvent(event: string, args: Record<string, Object>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | Session event name to dispatch |
| args | Record&lt;string, Object&gt; | 是 | The parameters of session event |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The asyncCallback triggered when the command is executed successfully |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [dispatchSessionEvent](#dispatchsessionevent)

## dispatchSessionEvent

```TypeScript
dispatchSessionEvent(event: string, args: {[key: string]: Object}): Promise<void>
```

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-dispatchSessionEvent(event: string, args: {[key: string]: Object}): Promise<void>--><!--Device-AVSession-dispatchSessionEvent(event: string, args: {[key: string]: Object}): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 需要设置的会话事件的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的会话事件内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当事件设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [dispatchSessionEvent](#dispatchsessionevent)

## dispatchSessionEvent

```TypeScript
dispatchSessionEvent(event: string, args: Record<string, Object>): Promise<void>
```

Dispatch the session event of this session.

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-dispatchSessionEvent(event: string, args: Record<string, Object>): Promise<void>--><!--Device-AVSession-dispatchSessionEvent(event: string, args: Record<string, Object>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | Session event name to dispatch |
| args | Record&lt;string, Object&gt; | 是 | The parameters of session event |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [dispatchSessionEvent](#dispatchsessionevent)

## enableDesktopLyric

```TypeScript
enableDesktopLyric(enable: boolean): Promise<void>
```

当前会话是否启用桌面歌词功能。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-enableDesktopLyric(enable: boolean): Promise<void>--><!--Device-AVSession-enableDesktopLyric(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用桌面歌词。true表示启用，false表示不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) | The desktop lyrics feature is not supported. |

**示例**

```TypeScript
currentAVSession.enableDesktopLyric(true).then(() => {
    console.info('Succeeded in enabling desktop lyric.');
});
```

## getAllCastDisplays

```TypeScript
getAllCastDisplays(): Promise<Array<CastDisplayInfo>>
```

获取当前系统中所有支持扩展屏投播的显示设备。通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-getAllCastDisplays(): Promise<Array<CastDisplayInfo>>--><!--Device-AVSession-getAllCastDisplays(): Promise<Array<CastDisplayInfo>>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[CastDisplayInfo](arkts-avsession-avsession-castdisplayinfo-i.md)&gt;&gt; | Promise对象，返回当前系统中所有支持扩展屏投播的显示设备。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
let castDisplay: avSession.CastDisplayInfo;
currentAVSession.getAllCastDisplays().then((data: Array< avSession.CastDisplayInfo >) => {
  if (data.length >= 1) {
    castDisplay = data[0];
  }
});
```

## getAVCastController

```TypeScript
getAVCastController(callback: AsyncCallback<AVCastController>): void
```

设备建立连接后，获取投播控制器。结果通过callback异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**起始版本：** 10

<!--Device-AVSession-getAVCastController(callback: AsyncCallback<AVCastController>): void--><!--Device-AVSession-getAVCastController(callback: AsyncCallback<AVCastController>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md)&gt; | 是 | 回调函数，返回投播控制器实例。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) | The remote connection is not established |

**示例**

```TypeScript
let avCastController: avSession.AVCastController;
currentAVSession.getAVCastController().then((avcontroller: avSession.AVCastController) => {
  avCastController = avcontroller;
  console.info('Succeeded in getting AV cast controller.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avCastController: avSession.AVCastController;
currentAVSession.getAVCastController((err: BusinessError, avcontroller: avSession.AVCastController) => {
  if (err) {
    console.error(`Failed to get AV cast controller, code: ${err.code}, message: ${err.message}`);
    return;
  }
  avCastController = avcontroller;
  console.info('Succeeded in getting AV cast controller.');
});
```

```TypeScript
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(async () => {
          // 获取当前系统中所有session的描述符。
          let descriptors = await AVSessionManager.getAllSessionDescriptors();
          if (descriptors.length === 0) {
            console.error(`No session in system, can not create controller.`);
            return;
          }
          // 取目标session的sessionId创建controller。
          let sessionId = descriptors[0].sessionId;

          let avCastController: avSession.AVCastController;
          avSession.getAVCastController(sessionId, (avcontroller: avSession.AVCastController) => {
              avCastController = avcontroller;
              console.info('Succeeded in getting AV cast controller.');
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## getAVCastController

```TypeScript
getAVCastController(callback: AsyncCallback<AVCastController | undefined>): void
```

Get the cast controller when the session is casted to remote device. If the avsession is not under casting state, the controller will return undefined.

**起始版本：** 23

<!--Device-AVSession-getAVCastController(callback: AsyncCallback<AVCastController | undefined>): void--><!--Device-AVSession-getAVCastController(callback: AsyncCallback<AVCastController | undefined>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md) \| undefined&gt; | 是 | async callback for the AVCastController. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) | The remote connection is not established |

**示例**

参见 [getAVCastController](#getavcastcontroller)

## getAVCastController

```TypeScript
getAVCastController(): Promise<AVCastController>
```

设备建立连接后，获取投播控制器。结果通过Promise异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-getAVCastController(): Promise<AVCastController>--><!--Device-AVSession-getAVCastController(): Promise<AVCastController>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md)&gt; | Promise对象。返回投播控制器实例。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) | The remote connection is not established |

**示例**

参见 [getAVCastController](#getavcastcontroller)

## getAVCastController

```TypeScript
getAVCastController(): Promise<AVCastController | undefined>
```

Get the cast controller when the session is casted to remote device. If the avsession is not under casting state, the controller will return undefined.

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-getAVCastController(): Promise<AVCastController | undefined>--><!--Device-AVSession-getAVCastController(): Promise<AVCastController | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AVCastController](arkts-avsession-avsession-avcastcontroller-i.md) \| undefined&gt; | Promise for the AVCastController |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) | The remote connection is not established |

**示例**

参见 [getAVCastController](#getavcastcontroller)

## getController

```TypeScript
getController(callback: AsyncCallback<AVSessionController>): void
```

获取本会话相应的控制器。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-getController(callback: AsyncCallback<AVSessionController>): void--><!--Device-AVSession-getController(callback: AsyncCallback<AVSessionController>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt; | 是 | 回调函数。返回会话控制器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.getController().then((avcontroller: avSession.AVSessionController) => {
  console.info(`Succeeded in getting controller, sessionid: ${avcontroller.sessionId}`);
});
```

```TypeScript
currentAVSession.getController((err: BusinessError, avcontroller: avSession.AVSessionController) => {
  if (err) {
    console.error(`Failed to get controller, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting controller, sessionid: ${avcontroller.sessionId}`);
});
```

## getController

```TypeScript
getController(): Promise<AVSessionController>
```

获取本会话对应的控制器。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-getController(): Promise<AVSessionController>--><!--Device-AVSession-getController(): Promise<AVSessionController>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt; | Promise对象。返回会话控制器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [getController](#getcontroller)

## getDesktopLyricState

```TypeScript
getDesktopLyricState(): Promise<DesktopLyricState>
```

获取当前会话桌面歌词状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-getDesktopLyricState(): Promise<DesktopLyricState>--><!--Device-AVSession-getDesktopLyricState(): Promise<DesktopLyricState>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md)&gt; | Promise对象。返回桌面歌词状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |
| [6600110](../errorcode-avsession.md#6600110-应用程序的桌面歌词功能未开启) | The desktop lyrics feature of this application is not enabled. |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) | The desktop lyrics feature is not supported. |

**示例**

```TypeScript
if (currentAVSession !== undefined) {
  (currentAVSession as avSession.AVSession).getDesktopLyricState()
    .then((state: avSession.DesktopLyricState) => {
    console.info(`getDesktopLyricState: ${state.isLocked}`);
  })
}
```

```TypeScript
currentAVSession.getDesktopLyricState()
    .then((state: avSession.DesktopLyricState) => {
    console.info(`getDesktopLyricState: ${state.isLocked}`);
});
```

```TypeScript
avcontroller.getDesktopLyricState();
```

## getOutputDevice

```TypeScript
getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void
```

通过会话获取播放设备相关信息。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void--><!--Device-AVSession-getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | 是 | 回调函数，返回播放设备信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.getOutputDevice().then((outputDeviceInfo: avSession.OutputDeviceInfo) => {
  console.info(`Succeeded in getting output device, devices length: ${outputDeviceInfo.devices.length}`);
})
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.getOutputDevice((err: BusinessError, outputDeviceInfo: avSession.OutputDeviceInfo) => {
  if (err) {
    console.error(`Failed to get output device, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting output device, devices length: ${outputDeviceInfo.devices.length}`);
});
```

```TypeScript
avcontroller.getOutputDevice().then((deviceInfo: avSession.OutputDeviceInfo) => {
  console.info('Succeeded in getting output device.');
});
```

```TypeScript
avcontroller.getOutputDevice((err: BusinessError, deviceInfo: avSession.OutputDeviceInfo) => {
  if (err) {
    console.error(`Failed to get output device, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting output device.');
});
```

## getOutputDevice

```TypeScript
getOutputDevice(): Promise<OutputDeviceInfo>
```

通过会话获取播放设备信息。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-getOutputDevice(): Promise<OutputDeviceInfo>--><!--Device-AVSession-getOutputDevice(): Promise<OutputDeviceInfo>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | Promise对象。返回播放设备信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [getOutputDevice](#getoutputdevice)

## getOutputDeviceSync

```TypeScript
getOutputDeviceSync(): OutputDeviceInfo
```

使用同步方法获取当前输出设备信息。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-getOutputDeviceSync(): OutputDeviceInfo--><!--Device-AVSession-getOutputDeviceSync(): OutputDeviceInfo-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) | 当前输出设备信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
let currentOutputDevice: avSession.OutputDeviceInfo = currentAVSession.getOutputDeviceSync();
```

```TypeScript
let currentOutputDevice: avSession.OutputDeviceInfo = avcontroller.getOutputDeviceSync();
```

## isDesktopLyricVisible

```TypeScript
isDesktopLyricVisible(): Promise<boolean>
```

查询当前会话桌面歌词的显示状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-isDesktopLyricVisible(): Promise<boolean>--><!--Device-AVSession-isDesktopLyricVisible(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示显示桌面歌词；返回false表示不显示桌面歌词。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |
| [6600110](../errorcode-avsession.md#6600110-应用程序的桌面歌词功能未开启) | The desktop lyrics feature of this application is not enabled. |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) | The desktop lyrics feature is not supported. |

**示例**

```TypeScript
currentAVSession.isDesktopLyricVisible().then((visible: boolean) => {
  console.info(`isDesktopLyricVisible: ${visible}`);
});
```

```TypeScript
currentAVSession.isDesktopLyricVisible().then((visible: boolean) => {
  console.info(`isDesktopLyricVisible: ${visible}`);
});
```

```TypeScript
avcontroller.isDesktopLyricVisible();
```

## off('answer')

```TypeScript
off(type: 'answer', callback?: Callback<void>): void
```

取消通话接听事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'answer', callback?: Callback<void>): void--><!--Device-AVSession-off(type: 'answer', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'answer' | 是 | 关闭对应的监听事件，支持的事件是`'answer'`。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('castDisplayChange')

```TypeScript
off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void
```

取消扩展屏投播显示设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void--><!--Device-AVSession-off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'castDisplayChange' | 是 | 关闭对应的监听事件，支持的事件是`'castDisplayChange'`。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CastDisplayInfo](arkts-avsession-avsession-castdisplayinfo-i.md)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会 话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |

## off('commonCommand')

```TypeScript
off(type: 'commonCommand', callback?: (command: string, args: {[key: string]: Object}) => void): void
```

取消自定义控制命令的变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'commonCommand', callback?: (command: string, args: {[key: string]: Object}) => void): void--><!--Device-AVSession-off(type: 'commonCommand', callback?: (command: string, args: {[key: string]: Object}) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'commonCommand' | 是 | 取消对应的监听事件，支持事件`'commonCommand'`。 |
| callback | (command: string, args: {[key: string]: Object}) =&gt; void | 否 | 回调函数，参数command是变化的自定义控制命令名，args为自定义控制命令的参数。 <br>该参数为可选参数，若不填写该参数，则认为取消所有对command事件的监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('customDataChange')

```TypeScript
off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void
```

Unsubscribes from custom data changes.

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void--><!--Device-AVSession-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'customDataChange' | 是 | Custom data type. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 否 | Callback used to return the custom data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('fastForward')

```TypeScript
off(type: 'fastForward', callback?: () => void): void
```

取消会话快进事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'fastForward', callback?: () => void): void--><!--Device-AVSession-off(type: 'fastForward', callback?: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'fastForward' | 是 | 关闭对应的监听事件，支持的事件是`'fastForward'`。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('handleKeyEvent')

```TypeScript
off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void
```

取消按键事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void--><!--Device-AVSession-off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'handleKeyEvent' | 是 | 关闭对应的监听事件，支持关闭事件`'handleKeyEvent'`。 |
| callback | (event: KeyEvent) =&gt; void | 否 | 回调函数，参数event是按键事件。 <br>当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('hangUp')

```TypeScript
off(type: 'hangUp', callback?: Callback<void>): void
```

取消通话挂断事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'hangUp', callback?: Callback<void>): void--><!--Device-AVSession-off(type: 'hangUp', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'hangUp' | 是 | 关闭对应的监听事件，支持的事件是`'hangUp'`。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('outputDeviceChange')

```TypeScript
off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void
```

取消播放设备变化的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void--><!--Device-AVSession-off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'outputDeviceChange' | 是 | 关闭对应的监听事件，支持关闭事件`'outputDeviceChange'`。 |
| callback | (state: ConnectionState, device: OutputDeviceInfo) =&gt; void | 否 | 回调函数，参数device是设备相关信息。 <br>当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |

## off('pause')

```TypeScript
off(type: 'pause', callback?: () => void): void
```

取消会话暂停事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'pause', callback?: () => void): void--><!--Device-AVSession-off(type: 'pause', callback?: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'pause' | 是 | 关闭对应的监听事件，支持的事件是`'pause'`。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('play')

```TypeScript
off(type: 'play', callback?: () => void): void
```

取消会话播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'play', callback?: () => void): void--><!--Device-AVSession-off(type: 'play', callback?: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' | 是 | 关闭对应的监听事件，支持的事件是`'play'`。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('playFromAssetId')

```TypeScript
off(type: 'playFromAssetId', callback?: (assetId: number) => void): void
```

取消媒体ID播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

> **说明：**&gt;
> 从API version 11开始支持，从API version 20开始废弃。建议使用
> [off('playWithAssetId')](#offplay)取消
> 媒体ID播放事件监听。

**起始版本：** 11

**废弃版本：** 20

**替代接口：** off

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'playFromAssetId', callback?: (assetId: number) => void): void--><!--Device-AVSession-off(type: 'playFromAssetId', callback?: (assetId: number) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playFromAssetId' | 是 | 关闭对应的监听事件，支持的事件是`'playFromAssetId'`。 |
| callback | (assetId: number) =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('playNext')

```TypeScript
off(type: 'playNext', callback?: () => void): void
```

取消会话播放下一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'playNext', callback?: () => void): void--><!--Device-AVSession-off(type: 'playNext', callback?: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playNext' | 是 | 关闭对应的监听事件，支持的事件是 `'playNext'`。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('playPrevious')

```TypeScript
off(type: 'playPrevious', callback?: () => void): void
```

取消会话播放上一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'playPrevious', callback?: () => void): void--><!--Device-AVSession-off(type: 'playPrevious', callback?: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playPrevious' | 是 | 关闭对应的监听事件，支持的事件是`'playPrevious'`。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('playWithAssetId')

```TypeScript
off(type: 'playWithAssetId', callback?: Callback<string>): void
```

取消指定资源id进行播放的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'playWithAssetId', callback?: Callback<string>): void--><!--Device-AVSession-off(type: 'playWithAssetId', callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playWithAssetId' | 是 | 关闭对应的监听事件，支持的事件是`'playWithAssetId'`。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('rewind')

```TypeScript
off(type: 'rewind', callback?: () => void): void
```

取消会话快退事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'rewind', callback?: () => void): void--><!--Device-AVSession-off(type: 'rewind', callback?: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'rewind' | 是 | 关闭对应的监听事件，支持的事件是`'rewind'`。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('seek')

```TypeScript
off(type: 'seek', callback?: (time: long) => void): void
```

取消跳转节点事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'seek', callback?: (time: long) => void): void--><!--Device-AVSession-off(type: 'seek', callback?: (time: long) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'seek' | 是 | 关闭对应的监听事件，支持关闭事件`'seek'`。 |
| callback | (time: long) =&gt; void | 否 | 回调函数，参数time是时间节点，单位为毫秒。 <br>当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('setLoopMode')

```TypeScript
off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void
```

取消循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void--><!--Device-AVSession-off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'setLoopMode' | 是 | 关闭对应的监听事件，支持关闭事件`'setLoopMode'`。 |
| callback | (mode: LoopMode) =&gt; void | 否 | 回调函数，参数mode是循环模式。 <br>- 当监听事件取消成功，err为undefined，否则返回错误对象。 <br>- 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('setSpeed')

```TypeScript
off(type: 'setSpeed', callback?: (speed: double) => void): void
```

取消播放速率变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'setSpeed', callback?: (speed: double) => void): void--><!--Device-AVSession-off(type: 'setSpeed', callback?: (speed: double) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'setSpeed' | 是 | 关闭对应的监听事件，支持关闭事件`'setSpeed'`。 |
| callback | (speed: double) =&gt; void | 否 | 回调函数，参数speed是播放倍速。 <br>当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('setTargetLoopMode')

```TypeScript
off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void
```

取消目标循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void--><!--Device-AVSession-off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'setTargetLoopMode' | 是 | 关闭对应的监听事件，支持关闭事件`'setTargetLoopMode'`。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt; | 否 | 回调函数，参数表示目标循环模式。 <br>- 当监听事件取消成功，err为undefined，否则返回错误对象。 <br>- 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('skipToQueueItem')

```TypeScript
off(type: 'skipToQueueItem', callback?: (itemId: int) => void): void
```

取消播放列表单项选中的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'skipToQueueItem', callback?: (itemId: int) => void): void--><!--Device-AVSession-off(type: 'skipToQueueItem', callback?: (itemId: int) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'skipToQueueItem' | 是 | 关闭对应的监听事件，支持关闭事件`'skipToQueueItem'`。 |
| callback | (itemId: int) =&gt; void | 否 | 回调函数，参数itemId是播放列表单项ID。 <br>当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('stop')

```TypeScript
off(type: 'stop', callback?: () => void): void
```

取消会话停止事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'stop', callback?: () => void): void--><!--Device-AVSession-off(type: 'stop', callback?: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'stop' | 是 | 关闭对应的监听事件，支持的事件是`'stop'`。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('toggleCallMute')

```TypeScript
off(type: 'toggleCallMute', callback?: Callback<void>): void
```

取消通话静音事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'toggleCallMute', callback?: Callback<void>): void--><!--Device-AVSession-off(type: 'toggleCallMute', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'toggleCallMute' | 是 | 关闭对应的监听事件，支持的事件是`'toggleCallMute'`。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## off('toggleFavorite')

```TypeScript
off(type: 'toggleFavorite', callback?: (assetId: string) => void): void
```

取消是否收藏的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-off(type: 'toggleFavorite', callback?: (assetId: string) => void): void--><!--Device-AVSession-off(type: 'toggleFavorite', callback?: (assetId: string) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'toggleFavorite' | 是 | 关闭对应的监听事件，支持关闭事件`'toggleFavorite'`。 |
| callback | (assetId: string) =&gt; void | 否 | 回调函数，参数assetId是媒体ID。 <br>当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## offAnswer

```TypeScript
offAnswer(callback?: NoParamCallback): void
```

Unregister answer command callback.

**起始版本：** 23

<!--Device-AVSession-offAnswer(callback?: NoParamCallback): void--><!--Device-AVSession-offAnswer(callback?: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 否 | Used to handle ('answer') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offAnswer();
```

## offCastDisplayChange

```TypeScript
offCastDisplayChange(callback?: Callback<CastDisplayInfo>): void
```

Unregister listener for cast display information changed.

**起始版本：** 23

<!--Device-AVSession-offCastDisplayChange(callback?: Callback<CastDisplayInfo>): void--><!--Device-AVSession-offCastDisplayChange(callback?: Callback<CastDisplayInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CastDisplayInfo](arkts-avsession-avsession-castdisplayinfo-i.md)&gt; | 否 | Callback used to return cast display information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |

**示例**

```TypeScript
currentAVSession.offCastDisplayChange();
```

## offCommonCommand

```TypeScript
offCommonCommand(callback?: EventProcess): void
```

Unregister session custom command change callback

**起始版本：** 23

<!--Device-AVSession-offCommonCommand(callback?: EventProcess): void--><!--Device-AVSession-offCommonCommand(callback?: EventProcess): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [EventProcess](arkts-avsession-avsession-eventprocess-t.md) | 否 | Used to cancel a specific listener The callback provide the command name and command args |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offCommonCommand();
```

## offCustomDataChange

```TypeScript
offCustomDataChange(callback?: Callback<Record<string, Object>>): void
```

Unsubscribes from custom data changes.

**起始版本：** 23

<!--Device-AVSession-offCustomDataChange(callback?: Callback<Record<string, Object>>): void--><!--Device-AVSession-offCustomDataChange(callback?: Callback<Record<string, Object>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 否 | Callback used to return the custom data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
avCastController.offCustomDataChange(callback);
```

```TypeScript
currentAVSession.offCustomDataChange();
```

```TypeScript
avcontroller.offCustomDataChange();
```

## offDesktopLyricStateChanged

```TypeScript
offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void
```

取消桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void--><!--Device-AVSession-offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有桌面歌词状态变更事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
try {
  currentAVSession.offDesktopLyricStateChanged();
} catch (err) {
  console.error(`Failed to unregister desktop lyric state changed, code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
if (currentAVSession !== undefined) {
  (currentAVSession as avSession.AVSession).offDesktopLyricStateChanged();
}
```

```TypeScript
avcontroller.offDesktopLyricStateChanged();
```

## offDesktopLyricVisibilityChanged

```TypeScript
offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void
```

取消显示桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void--><!--Device-AVSession-offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有显示桌面歌词状态变更事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
if (currentAVSession !== undefined) {
  (currentAVSession as avSession.AVSession).offDesktopLyricVisibilityChanged();
}
```

```TypeScript
if (currentAVSession !== undefined) {
  (currentAVSession as avSession.AVSession).offDesktopLyricVisibilityChanged();
}
```

```TypeScript
avcontroller.offDesktopLyricVisibilityChanged();
```

## offFastForward

```TypeScript
offFastForward(callback?: TwoParamCallback<long, CommandInfo>): void
```

取消会话快进事件监听。使用callback异步回调。指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**起始版本：** 23

<!--Device-AVSession-offFastForward(callback?: TwoParamCallback<long, CommandInfo>): void--><!--Device-AVSession-offFastForward(callback?: TwoParamCallback<long, CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TwoParamCallback](arkts-avsession-avsession-twoparamcallback-t.md)&lt;long, [CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offFastForward();
```

## offHandleKeyEvent

```TypeScript
offHandleKeyEvent(callback?: Callback<KeyEvent>): void
```

Unregister media key handling callback

**起始版本：** 23

<!--Device-AVSession-offHandleKeyEvent(callback?: Callback<KeyEvent>): void--><!--Device-AVSession-offHandleKeyEvent(callback?: Callback<KeyEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | 否 | Used to handle key events.The callback provides the KeyEvent |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offHandleKeyEvent();
```

## offHangUp

```TypeScript
offHangUp(callback?: NoParamCallback): void
```

Unregister hangUp command callback.

**起始版本：** 23

<!--Device-AVSession-offHangUp(callback?: NoParamCallback): void--><!--Device-AVSession-offHangUp(callback?: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 否 | Used to handle ('hangUp') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offHangUp();
```

## offOutputDeviceChange

```TypeScript
offOutputDeviceChange(callback?: ConnectionEvent): void
```

Unregister session output device change callback

**起始版本：** 23

<!--Device-AVSession-offOutputDeviceChange(callback?: ConnectionEvent): void--><!--Device-AVSession-offOutputDeviceChange(callback?: ConnectionEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ConnectionEvent](arkts-avsession-avsession-connectionevent-t.md) | 否 | Used to handle output device changed. The callback provide the new device info [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) and related connection state [ConnectionState](arkts-avsession-avsession-connectionstate-e.md). |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |

**示例**

```TypeScript
currentAVSession.offOutputDeviceChange();
```

```TypeScript
avcontroller.offOutputDeviceChange();
```

## offPause

```TypeScript
offPause(callback?: NoParamCallback): void
```

Unregister pause command callback. When canceling the callback, need to update the supported commands list.

**起始版本：** 23

<!--Device-AVSession-offPause(callback?: NoParamCallback): void--><!--Device-AVSession-offPause(callback?: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 否 | Used to handle ('pause') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offPause();
```

## offPlay

```TypeScript
offPlay(callback?: Callback<CommandInfo>): void
```

取消会话播放事件监听。使用callback异步回调。指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**起始版本：** 23

<!--Device-AVSession-offPlay(callback?: Callback<CommandInfo>): void--><!--Device-AVSession-offPlay(callback?: Callback<CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offPlay();
```

## offPlayNext

```TypeScript
offPlayNext(callback?: Callback<CommandInfo>): void
```

取消会话播放下一首事件监听。使用callback异步回调。指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**起始版本：** 23

<!--Device-AVSession-offPlayNext(callback?: Callback<CommandInfo>): void--><!--Device-AVSession-offPlayNext(callback?: Callback<CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
avCastController.offPlayNext();
```

```TypeScript
currentAVSession.offPlayNext();
```

## offPlayPrevious

```TypeScript
offPlayPrevious(callback?: Callback<CommandInfo>): void
```

取消会话播放上一首事件监听。使用callback异步回调。指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**起始版本：** 23

<!--Device-AVSession-offPlayPrevious(callback?: Callback<CommandInfo>): void--><!--Device-AVSession-offPlayPrevious(callback?: Callback<CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
avCastController.offPlayPrevious();
```

```TypeScript
currentAVSession.offPlayPrevious();
```

## offPlayWithAssetId

```TypeScript
offPlayWithAssetId(callback?: Callback<string>): void
```

Unsubscribes from playWithAssetId events.

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-offPlayWithAssetId(callback?: Callback<string>): void--><!--Device-AVSession-offPlayWithAssetId(callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 | Callback used to handle the 'playWithAssetId' command. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offPlayWithAssetId();
```

## offRewind

```TypeScript
offRewind(callback?: TwoParamCallback<long, CommandInfo>): void
```

取消会话快退事件监听。使用callback异步回调。指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**起始版本：** 23

<!--Device-AVSession-offRewind(callback?: TwoParamCallback<long, CommandInfo>): void--><!--Device-AVSession-offRewind(callback?: TwoParamCallback<long, CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TwoParamCallback](arkts-avsession-avsession-twoparamcallback-t.md)&lt;long, [CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offRewind();
```

## offSeek

```TypeScript
offSeek(callback?: Callback<long>): void
```

Unregister seek command callback

**起始版本：** 23

<!--Device-AVSession-offSeek(callback?: Callback<long>): void--><!--Device-AVSession-offSeek(callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | Used to handle seek command.The callback provides the seek time(ms) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offSeek();
```

## offSetLoopMode

```TypeScript
offSetLoopMode(callback?: Callback<LoopMode>): void
```

Unregister setLoopMode command callback

**起始版本：** 23

<!--Device-AVSession-offSetLoopMode(callback?: Callback<LoopMode>): void--><!--Device-AVSession-offSetLoopMode(callback?: Callback<LoopMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt; | 否 | Used to handle setLoopMode command. The callback provides the [LoopMode](arkts-avsession-avsession-loopmode-e.md) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offSetLoopMode();
```

## offSetSpeed

```TypeScript
offSetSpeed(callback?: Callback<double>): void
```

Unregister setSpeed command callback

**起始版本：** 23

<!--Device-AVSession-offSetSpeed(callback?: Callback<double>): void--><!--Device-AVSession-offSetSpeed(callback?: Callback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;double&gt; | 否 | Used to handle setSpeed command.The callback provides the speed value |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offSetSpeed();
```

## offSetTargetLoopMode

```TypeScript
offSetTargetLoopMode(callback?: Callback<LoopMode>): void
```

Unregister setTargetLoopMode command callback

**起始版本：** 23

<!--Device-AVSession-offSetTargetLoopMode(callback?: Callback<LoopMode>): void--><!--Device-AVSession-offSetTargetLoopMode(callback?: Callback<LoopMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt; | 否 | Used to handle setTargetLoopMode command. The callback provides the [LoopMode](arkts-avsession-avsession-loopmode-e.md) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offSetTargetLoopMode();
```

## offSkipToQueueItem

```TypeScript
offSkipToQueueItem(callback?: Callback<int>): void
```

Unregister the item to play from the playlist change callback

**起始版本：** 23

<!--Device-AVSession-offSkipToQueueItem(callback?: Callback<int>): void--><!--Device-AVSession-offSkipToQueueItem(callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 | Used to handle the item to be played. The callback provide the new device info [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offSkipToQueueItem();
```

## offStop

```TypeScript
offStop(callback?: NoParamCallback): void
```

Unregister stop command callback. When canceling the callback, need to update the supported commands list.

**起始版本：** 23

<!--Device-AVSession-offStop(callback?: NoParamCallback): void--><!--Device-AVSession-offStop(callback?: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 否 | Used to handle ('stop') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offStop();
```

## offToggleCallMute

```TypeScript
offToggleCallMute(callback?: NoParamCallback): void
```

Unregister toggleCallMute command callback.

**起始版本：** 23

<!--Device-AVSession-offToggleCallMute(callback?: NoParamCallback): void--><!--Device-AVSession-offToggleCallMute(callback?: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 否 | Used to handle ('toggleCallMute') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offToggleCallMute();
```

## offToggleFavorite

```TypeScript
offToggleFavorite(callback?: Callback<string>): void
```

Unregister toggle favorite command callback

**起始版本：** 23

<!--Device-AVSession-offToggleFavorite(callback?: Callback<string>): void--><!--Device-AVSession-offToggleFavorite(callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 | Used to handle toggleFavorite command.The callback provides the assetId for which the favorite status needs to be switched. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.offToggleFavorite();
```

## on('answer')

```TypeScript
on(type: 'answer', callback: Callback<void>): void
```

设置通话接听的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'answer', callback: Callback<void>): void--><!--Device-AVSession-on(type: 'answer', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'answer' | 是 | 事件回调类型，支持事件`'answer'`：当通话接听时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('castDisplayChange')

```TypeScript
on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void
```

设置扩展屏投播显示设备变化的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void--><!--Device-AVSession-on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'castDisplayChange' | 是 | 事件回调类型，支持事件`'castDisplayChange'`：当扩展屏投播显示设备变化时触发事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CastDisplayInfo](arkts-avsession-avsession-castdisplayinfo-i.md)&gt; | 是 | 回调函数。参数是扩展屏投播显示设备信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |

## on('commonCommand')

```TypeScript
on(type: 'commonCommand', callback: (command: string, args: {[key: string]: Object}) => void): void
```

设置自定义控制命令变化的监听器。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'commonCommand', callback: (command: string, args: {[key: string]: Object}) => void): void--><!--Device-AVSession-on(type: 'commonCommand', callback: (command: string, args: {[key: string]: Object}) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'commonCommand' | 是 | 事件回调类型，支持事件`'commonCommand'`：当自定义控制命令变化时，触发该事件。 |
| callback | (command: string, args: {[key: string]: Object}) =&gt; void | 是 | 回调函数，command为变化的自定义控制命令名，args为自定义控制命令的参数，参数内容与 sendCommonCommand)} 方法设置的参数内容完全一致。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('customDataChange')

```TypeScript
on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void
```

注册从远程设备发送的自定义数据的监听器。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void--><!--Device-AVSession-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'customDataChange' | 是 | 事件回调类型，支持事件'customDataChange'，当媒体提供方发送自定义数据时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 是 | 回调函数，用于接收自定义数据。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('fastForward')

```TypeScript
on(type: 'fastForward', callback: (time ?: long) => void): void
```

设置快进命令监听事件。注册该监听，说明应用支持快进指令。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'fastForward', callback: (time ?: long) => void): void--><!--Device-AVSession-on(type: 'fastForward', callback: (time ?: long) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'fastForward' | 是 | 事件回调类型，支持的事件是 `'fastForward'`，当快进命令被发送到会话时，触发该事件回调。 |
| callback | (time ?: long) =&gt; void | 是 | 回调函数。参数time是时间节点，单位为秒。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('handleKeyEvent')

```TypeScript
on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void
```

设置蓝牙/有线等外设接入的按键输入事件的监听，监听多媒体按键事件中播放、暂停、上下一首、快进、快退的指令。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void--><!--Device-AVSession-on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'handleKeyEvent' | 是 | 事件回调类型，支持事件`'handleKeyEvent'`：当按键事件被发送到会话时，触发该事件。 |
| callback | (event: KeyEvent) =&gt; void | 是 | 回调函数。参数event是按键事件。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('hangUp')

```TypeScript
on(type: 'hangUp', callback: Callback<void>): void
```

设置通话挂断的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'hangUp', callback: Callback<void>): void--><!--Device-AVSession-on(type: 'hangUp', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'hangUp' | 是 | 事件回调类型，支持事件`'hangUp'`：当通话挂断时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('outputDeviceChange')

```TypeScript
on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void
```

设置播放设备变化的监听事件。应用接入[multimedia.avCastPicker (投播组件)](arkts-avsession-multimedia-avcastpicker-avcastpicker-s.md)，当用户通过组件切换设备 时，会收到设备切换的回调。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void--><!--Device-AVSession-on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'outputDeviceChange' | 是 | 事件回调类型，支持事件`'outputDeviceChange'`：当播放设备变化时，触发该事件。 |
| callback | (state: ConnectionState, device: OutputDeviceInfo) =&gt; void | 是 | 回调函数，参数device是设备相关信息。 <br>该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |

## on('pause')

```TypeScript
on(type: 'pause', callback: () => void): void
```

设置暂停命令监听事件。注册该监听，说明应用支持暂停指令。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'pause', callback: () => void): void--><!--Device-AVSession-on(type: 'pause', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'pause' | 是 | 事件回调类型，支持的事件为`'pause'`，当暂停命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('play')

```TypeScript
on(type: 'play', callback: () => void): void
```

设置播放命令监听事件。注册该监听，说明应用支持播放指令。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'play', callback: () => void): void--><!--Device-AVSession-on(type: 'play', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' | 是 | 事件回调类型，支持的事件为`'play'`，当播放命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('playFromAssetId')

```TypeScript
on(type: 'playFromAssetId', callback: (assetId: number) => void): void
```

设置媒体ID播放监听事件。

> **说明：**&gt;
> 从API version 11开始支持，从API version 20开始废弃。建议使用
> [on('playWithAssetId')](#onplay)设置媒体
> ID播放监听事件。

**起始版本：** 11

**废弃版本：** 20

**替代接口：** on

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'playFromAssetId', callback: (assetId: number) => void): void--><!--Device-AVSession-on(type: 'playFromAssetId', callback: (assetId: number) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playFromAssetId' | 是 | 事件回调类型，支持的事件是`'playFromAssetId'`，当媒体ID播放时，触发该事件回调。 |
| callback | (assetId: number) =&gt; void | 是 | 回调函数。参数assetId是媒体ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('playNext')

```TypeScript
on(type: 'playNext', callback: () => void): void
```

设置播放下一首命令监听事件。注册该监听，说明应用支持下一首指令。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'playNext', callback: () => void): void--><!--Device-AVSession-on(type: 'playNext', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playNext' | 是 | 事件回调类型，支持的事件是`'playNext'`，当播放下一首命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('playPrevious')

```TypeScript
on(type: 'playPrevious', callback: () => void): void
```

设置播放上一首命令监听事件。注册该监听，说明应用支持上一首指令。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'playPrevious', callback: () => void): void--><!--Device-AVSession-on(type: 'playPrevious', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playPrevious' | 是 | 事件回调类型，支持的事件是`'playPrevious'`，当播放上一首命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('playWithAssetId')

```TypeScript
on(type: 'playWithAssetId', callback: Callback<string>): void
```

设置指定资源id进行播放的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'playWithAssetId', callback: Callback<string>): void--><!--Device-AVSession-on(type: 'playWithAssetId', callback: Callback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playWithAssetId' | 是 | 事件回调类型，支持的事件是`'playWithAssetId'`，当指定资源id进行播放时，触发该事件回调。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 | 回调函数。参数assetId是媒体ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('rewind')

```TypeScript
on(type: 'rewind', callback: (time ?: long) => void): void
```

设置快退命令监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'rewind', callback: (time ?: long) => void): void--><!--Device-AVSession-on(type: 'rewind', callback: (time ?: long) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'rewind' | 是 | 事件回调类型，支持的事件是`'rewind'`，当快退命令被发送到会话时，触发该事件回调。 |
| callback | (time ?: long) =&gt; void | 是 | 回调函数。参数time是时间节点，单位为秒。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('seek')

```TypeScript
on(type: 'seek', callback: (time: long) => void): void
```

设置跳转节点监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'seek', callback: (time: long) => void): void--><!--Device-AVSession-on(type: 'seek', callback: (time: long) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'seek' | 是 | 事件回调类型，支持事件`'seek'`：当跳转节点命令被发送到会话时，触发该事件。 |
| callback | (time: long) =&gt; void | 是 | 回调函数。参数time是时间节点，单位为毫秒。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('setLoopMode')

```TypeScript
on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void
```

设置循环模式的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void--><!--Device-AVSession-on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'setLoopMode' | 是 | 事件回调类型，支持事件`'setLoopMode'`：当设置循环模式的命令被发送到会话时，触发该事件。 |
| callback | (mode: LoopMode) =&gt; void | 是 | 回调函数。参数mode是循环模式。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('setSpeed')

```TypeScript
on(type: 'setSpeed', callback: (speed: double) => void): void
```

设置播放速率的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'setSpeed', callback: (speed: double) => void): void--><!--Device-AVSession-on(type: 'setSpeed', callback: (speed: double) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'setSpeed' | 是 | 事件回调类型，支持事件`'setSpeed'`：当设置播放速率的命令被发送到会话时，触发该事件。 |
| callback | (speed: double) =&gt; void | 是 | 回调函数。参数speed是播放倍速。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('setTargetLoopMode')

```TypeScript
on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void
```

设置目标循环模式的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void--><!--Device-AVSession-on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'setTargetLoopMode' | 是 | 事件回调类型，支持事件`'setTargetLoopMode'`。 <br>- `'setTargetLoopMode'`：当设置目标循环模式的命令被发送到会话时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt; | 是 | 回调函数。参数表示目标循环模式。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('skipToQueueItem')

```TypeScript
on(type: 'skipToQueueItem', callback: (itemId: int) => void): void
```

设置播放列表其中某项被选中的监听事件，session端可以选择对这个单项歌曲进行播放。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'skipToQueueItem', callback: (itemId: int) => void): void--><!--Device-AVSession-on(type: 'skipToQueueItem', callback: (itemId: int) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'skipToQueueItem' | 是 | 事件回调类型，支持事件`'skipToQueueItem'`：当播放列表选中单项的命令被发送到会话时，触发该事件。 |
| callback | (itemId: int) =&gt; void | 是 | 回调函数。参数itemId是选中的播放列表项的ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('stop')

```TypeScript
on(type: 'stop', callback: () => void): void
```

设置停止命令监听事件。注册该监听，说明应用支持停止指令。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'stop', callback: () => void): void--><!--Device-AVSession-on(type: 'stop', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'stop' | 是 | 事件回调类型，支持的事件是`'stop'`，当停止命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('toggleCallMute')

```TypeScript
on(type: 'toggleCallMute', callback: Callback<void>): void
```

设置通话静音的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'toggleCallMute', callback: Callback<void>): void--><!--Device-AVSession-on(type: 'toggleCallMute', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'toggleCallMute' | 是 | 事件回调类型，支持事件`'toggleCallMute'`：当通话静音或解除静音时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## on('toggleFavorite')

```TypeScript
on(type: 'toggleFavorite', callback: (assetId: string) => void): void
```

设置是否收藏的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-on(type: 'toggleFavorite', callback: (assetId: string) => void): void--><!--Device-AVSession-on(type: 'toggleFavorite', callback: (assetId: string) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'toggleFavorite' | 是 | 事件回调类型，支持事件`'toggleFavorite'`：当是否收藏的命令被发送到会话时，触发该事件。 |
| callback | (assetId: string) =&gt; void | 是 | 回调函数。参数assetId是媒体ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

## onAnswer

```TypeScript
onAnswer(callback: NoParamCallback): void
```

Register answer command callback. As long as it is registered, it means that the ability supports this command. If you cancel the callback, you need to call off off

**起始版本：** 23

<!--Device-AVSession-onAnswer(callback: NoParamCallback): void--><!--Device-AVSession-onAnswer(callback: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 是 | Used to handle ('answer') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onAnswer(() => {
  console.info('on call answer');
});
```

## onCastDisplayChange

```TypeScript
onCastDisplayChange(callback: Callback<CastDisplayInfo>): void
```

Register listener for cast display information changed.

**起始版本：** 23

<!--Device-AVSession-onCastDisplayChange(callback: Callback<CastDisplayInfo>): void--><!--Device-AVSession-onCastDisplayChange(callback: Callback<CastDisplayInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CastDisplayInfo](arkts-avsession-avsession-castdisplayinfo-i.md)&gt; | 是 | Callback used to return cast display information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |

**示例**

```TypeScript
let castDisplay: avSession.CastDisplayInfo;
currentAVSession.onCastDisplayChange((display: avSession.CastDisplayInfo) => {
  if (display.state === avSession.CastDisplayState.STATE_ON) {
    castDisplay = display;
    console.info(`Succeeded in castDisplayChange display : ${display.id} ON`);
  } else if (display.state === avSession.CastDisplayState.STATE_OFF){
    console.info(`Succeeded in castDisplayChange display : ${display.id} OFF`);
  }
});
```

## onCommonCommand

```TypeScript
onCommonCommand(callback: EventProcess): void
```

Register session custom command change callback

**起始版本：** 23

<!--Device-AVSession-onCommonCommand(callback: EventProcess): void--><!--Device-AVSession-onCommonCommand(callback: EventProcess): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [EventProcess](arkts-avsession-avsession-eventprocess-t.md) | 是 | Used to handle event when the common command is received The callback provide the command name and command args |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onCommonCommand((commonCommand, args) => {
  console.info(`OnCommonCommand, the command is ${commonCommand}, args: ${JSON.stringify(args)}`);
});
```

## onCustomDataChange

```TypeScript
onCustomDataChange(callback: Callback<Record<string, Object>>): void
```

Register listener for custom data sent from remote device.

**起始版本：** 23

<!--Device-AVSession-onCustomDataChange(callback: Callback<Record<string, Object>>): void--><!--Device-AVSession-onCustomDataChange(callback: Callback<Record<string, Object>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 是 | Callback used to retrieve custom data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
avCastController.onCustomDataChange((data: Record<string, Object>) => {
  console.info(`onCustomDataChange, data, code: ${err.code}, message, code: ${err.code}, message: ${JSON.stringify(data)}`);
});
```

```TypeScript
currentAVSession.onCustomDataChange((callback) =>
{
  console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
});
```

```TypeScript
avcontroller.onCustomDataChange((data: Record<string, Object>) => {
  console.info(`on_customDataChange Successfully ${data}`);
});
```

## onDesktopLyricStateChanged

```TypeScript
onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void
```

桌面歌词状态变更的监听事件。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void--><!--Device-AVSession-onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md)&gt; | 是 | 回调函数。返回桌面歌词状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
try {
  currentAVSession.onDesktopLyricStateChanged((state: avSession.DesktopLyricState) => {
    console.info(`desktop lyric isLocked : ${state.isLocked}`);
  });
} catch (err) {
  console.error(`Failed to register desktop lyric state changed, code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
if (currentAVSession !== undefined) {
  (currentAVSession as avSession.AVSession).onDesktopLyricStateChanged((state: avSession.DesktopLyricState) => {
    console.info(`desktop lyric isLocked : ${state.isLocked}`);
  })
}
```

```TypeScript
avcontroller.onDesktopLyricStateChanged((state: avSession.DesktopLyricState) => {
  console.info(`desktop lyric isLocked : ${state.isLocked}`);
});
```

## onDesktopLyricVisibilityChanged

```TypeScript
onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void
```

显示桌面歌词状态变更的监听事件。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void--><!--Device-AVSession-onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 | 回调函数。返回true表示开启显示桌面歌词状态；返回false表示关闭显示桌面歌词状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
if (currentAVSession !== undefined) {
  (currentAVSession as avSession.AVSession).onDesktopLyricVisibilityChanged((visible: boolean) => {
    console.info(`desktop lyric visible state: ${visible}`);
  });
}
```

```TypeScript
currentAVSession.onDesktopLyricVisibilityChanged((visible: boolean) => {
  console.info(`desktop lyric visible state: ${visible}`);
});
```

```TypeScript
avcontroller.onDesktopLyricVisibilityChanged((visible: boolean) => {
  console.info(`desktop lyric visible state: ${visible}`);
});
```

## onFastForward

```TypeScript
onFastForward(callback: TwoParamCallback<long, CommandInfo>): void
```

设置快进命令监听事件。使用callback异步回调。应用将通过回调接收控制器发送的快进时间参数，以及对应的[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)信息。

**起始版本：** 23

<!--Device-AVSession-onFastForward(callback: TwoParamCallback<long, CommandInfo>): void--><!--Device-AVSession-onFastForward(callback: TwoParamCallback<long, CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TwoParamCallback](arkts-avsession-avsession-twoparamcallback-t.md)&lt;long, [CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 是 | 回调函数。用于处理'fastForward'操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onFastForward((time: number, info: avSession.CommandInfo) => {
  console.info('on fastForward entry');
});
```

## onHandleKeyEvent

```TypeScript
onHandleKeyEvent(callback: Callback<KeyEvent>): void
```

Register media key handling callback

**起始版本：** 23

<!--Device-AVSession-onHandleKeyEvent(callback: Callback<KeyEvent>): void--><!--Device-AVSession-onHandleKeyEvent(callback: Callback<KeyEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | 是 | Used to handle key events.The callback provides the KeyEvent |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
import { KeyEvent } from '@kit.InputKit';

currentAVSession.onHandleKeyEvent((event: KeyEvent) => {
  console.info(`on handleKeyEvent event : ${event}`);
});
```

## onHangUp

```TypeScript
onHangUp(callback: NoParamCallback): void
```

Register hangUp command callback. As long as it is registered, it means that the ability supports this command. If you cancel the callback, you need to call off off

**起始版本：** 23

<!--Device-AVSession-onHangUp(callback: NoParamCallback): void--><!--Device-AVSession-onHangUp(callback: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 是 | Used to handle ('hangUp') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onHangUp(() => {
  console.info('on call hangUp');
});
```

## onOutputDeviceChange

```TypeScript
onOutputDeviceChange(callback: ConnectionEvent): void
```

Register session output device change callback

**起始版本：** 23

<!--Device-AVSession-onOutputDeviceChange(callback: ConnectionEvent): void--><!--Device-AVSession-onOutputDeviceChange(callback: ConnectionEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ConnectionEvent](arkts-avsession-avsession-connectionevent-t.md) | 是 | Used to handle output device changed. The callback provide the new device info [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) and related connection state [ConnectionState](arkts-avsession-avsession-connectionstate-e.md). |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist |

**示例**

```TypeScript
currentAVSession.onOutputDeviceChange((state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
  console.info(`onOutputDeviceChange device : ${device}`);
});
```

```TypeScript
avsessionController.onOutputDeviceChange((state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
  console.info(`onOutputDeviceChange state: ${state}, device : ${device}`);
});
```

## onPause

```TypeScript
onPause(callback: NoParamCallback): void
```

Register pause command callback. As long as it is registered, it means that the ability supports this command. If you cancel the callback, you need to call off off When canceling the callback, need to update the supported commands list. Each playback command only supports registering one callback, and the new callback will replace the previous one.

**起始版本：** 23

<!--Device-AVSession-onPause(callback: NoParamCallback): void--><!--Device-AVSession-onPause(callback: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 是 | Used to handle ('pause') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onPause(() => {
  console.info('onPause entry');
});
```

## onPlay

```TypeScript
onPlay(callback: Callback<CommandInfo>): void
```

设置播放命令监听事件。使用callback异步回调。应用将通过回调接收控制器发送的[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)信息。

**起始版本：** 23

<!--Device-AVSession-onPlay(callback: Callback<CommandInfo>): void--><!--Device-AVSession-onPlay(callback: Callback<CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onPlay((info: avSession.CommandInfo) => {
  console.info('on play entry');
});
```

## onPlayNext

```TypeScript
onPlayNext(callback: Callback<CommandInfo>): void
```

设置播放下一首命令监听事件。使用callback异步回调。应用将通过回调接收控制器发送的[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)信息。

**起始版本：** 23

<!--Device-AVSession-onPlayNext(callback: Callback<CommandInfo>): void--><!--Device-AVSession-onPlayNext(callback: Callback<CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
avCastController.onPlayNext(() => {
  console.info('onPlayNext');
});
```

```TypeScript
currentAVSession.onPlayNext((info: avSession.CommandInfo) => {
  console.info('on playNext entry');
});
```

## onPlayPrevious

```TypeScript
onPlayPrevious(callback: Callback<CommandInfo>): void
```

设置播放上一首命令监听事件。使用callback异步回调。应用将通过回调接收控制器发送的[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)信息。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-onPlayPrevious(callback: Callback<CommandInfo>): void--><!--Device-AVSession-onPlayPrevious(callback: Callback<CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
avCastController.onPlayPrevious(() => {
  console.info('onPlayPrevious');
});
```

```TypeScript
currentAVSession.onPlayPrevious((info: avSession.CommandInfo) => {
  console.info('on playPrevious entry');
});
```

## onPlayWithAssetId

```TypeScript
onPlayWithAssetId(callback: Callback<string>): void
```

Subscribes to playWithAssetId events.

**起始版本：** 23

<!--Device-AVSession-onPlayWithAssetId(callback: Callback<string>): void--><!--Device-AVSession-onPlayWithAssetId(callback: Callback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 | Callback used to handle the 'playWithAssetId' command. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
let playWithAssetIdCallback = (assetId: string) => {
  console.info(`on playWithAssetId entry,  assetId = ${assetId}`);
}
currentAVSession.onPlayWithAssetId(playWithAssetIdCallback);
```

## onRewind

```TypeScript
onRewind(callback: TwoParamCallback<long, CommandInfo>): void
```

设置快退命令监听事件。使用callback异步回调。应用将通过回调接收控制器发送的快退时间参数，以及对应的[CommandInfo](arkts-avsession-avsession-commandinfo-i.md)信息。

**起始版本：** 23

<!--Device-AVSession-onRewind(callback: TwoParamCallback<long, CommandInfo>): void--><!--Device-AVSession-onRewind(callback: TwoParamCallback<long, CommandInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TwoParamCallback](arkts-avsession-avsession-twoparamcallback-t.md)&lt;long, [CommandInfo](arkts-avsession-avsession-commandinfo-i.md)&gt; | 是 | 回调函数。用于处理'rewind'操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onRewind((time: number, info: avSession.CommandInfo) => {
  console.info('on rewind entry');
});
```

## onSeek

```TypeScript
onSeek(callback: Callback<long>): void
```

Register seek command callback

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-onSeek(callback: Callback<long>): void--><!--Device-AVSession-onSeek(callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 | Used to handle seek command.The callback provides the seek time(ms) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onSeek((time: long) => {
  console.info(`onSeek entry time : ${time}`);
});
```

## onSetLoopMode

```TypeScript
onSetLoopMode(callback: Callback<LoopMode>): void
```

Register setLoopMode command callback

**起始版本：** 23

<!--Device-AVSession-onSetLoopMode(callback: Callback<LoopMode>): void--><!--Device-AVSession-onSetLoopMode(callback: Callback<LoopMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt; | 是 | Used to handle setLoopMode command.The callback provides the [LoopMode](arkts-avsession-avsession-loopmode-e.md) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onSetLoopMode((mode: avSession.LoopMode) => {
  console.info(`onSetLoopMode mode : ${mode}`);
});
```

## onSetSpeed

```TypeScript
onSetSpeed(callback: Callback<double>): void
```

Register setSpeed command callback

**起始版本：** 23

<!--Device-AVSession-onSetSpeed(callback: Callback<double>): void--><!--Device-AVSession-onSetSpeed(callback: Callback<double>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;double&gt; | 是 | Used to handle setSpeed command.The callback provides the speed value |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onSetSpeed((speed: double) => {
  console.info(`onSetSpeed speed : ${speed}`);
});
```

## onSetTargetLoopMode

```TypeScript
onSetTargetLoopMode(callback: Callback<LoopMode>): void
```

Register setTargetLoopMode command callback Application should change playmode to the loopmode which is requested.

**起始版本：** 23

<!--Device-AVSession-onSetTargetLoopMode(callback: Callback<LoopMode>): void--><!--Device-AVSession-onSetTargetLoopMode(callback: Callback<LoopMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt; | 是 | Used to handle setTargetLoopMode command. The callback provides the [LoopMode](arkts-avsession-avsession-loopmode-e.md) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onSetTargetLoopMode((mode: avSession.LoopMode) => {
  console.info(`onSetTargetLoopMode mode : ${mode}`);
});
```

## onSkipToQueueItem

```TypeScript
onSkipToQueueItem(callback: Callback<int>): void
```

Register the item to play from the playlist change callback

**起始版本：** 23

<!--Device-AVSession-onSkipToQueueItem(callback: Callback<int>): void--><!--Device-AVSession-onSkipToQueueItem(callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 | Used to handle the item to be played. The callback provide the new device info [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onSkipToQueueItem((itemId: int) => {
  console.info(`onSkipToQueueItem id : ${itemId}`);
});
```

## onStop

```TypeScript
onStop(callback: NoParamCallback): void
```

Register stop command callback. As long as it is registered, it means that the ability supports this command. If you cancel the callback, you need to call off off When canceling the callback, need to update the supported commands list. Each playback command only supports registering one callback, and the new callback will replace the previous one.

**起始版本：** 23

<!--Device-AVSession-onStop(callback: NoParamCallback): void--><!--Device-AVSession-onStop(callback: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 是 | Used to handle ('stop') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onStop(() => {
  console.info('onStop entry');
});
```

## onToggleCallMute

```TypeScript
onToggleCallMute(callback: NoParamCallback): void
```

Register toggleCallMute command callback. As long as it is registered, it means that the ability supports this command. If you cancel the callback, you need to call off off

**起始版本：** 23

<!--Device-AVSession-onToggleCallMute(callback: NoParamCallback): void--><!--Device-AVSession-onToggleCallMute(callback: NoParamCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | 是 | Used to handle ('toggleCallMute') command |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onToggleCallMute(() => {
  console.info('on call toggleCallMute');
});
```

## onToggleFavorite

```TypeScript
onToggleFavorite(callback: Callback<string>): void
```

Register toggle favorite command callback

**起始版本：** 23

<!--Device-AVSession-onToggleFavorite(callback: Callback<string>): void--><!--Device-AVSession-onToggleFavorite(callback: Callback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 | Used to handle toggleFavorite command.The callback provides the assetId for which the favorite status needs to be switched. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.onToggleFavorite((assetId: string) => {
  console.info(`onToggleFavorite mode : ${assetId}`);
});
```

## sendCustomData

```TypeScript
sendCustomData(data: Record<string, Object>): Promise<void>
```

发送私有数据到远端设备。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-sendCustomData(data: Record<string, Object>): Promise<void>--><!--Device-AVSession-sendCustomData(data: Record<string, Object>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record&lt;string, Object&gt; | 是 | 应用程序填充的自定义数据。服务端仅解析key为'customData'，且Object为string类型的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
avCastController.sendCustomData({customData: 'This is custom data'}).then(() => {
  console.info('Succeeded in sending custom data.');
}).catch((err: BusinessError) => {
  console.error(`Failed to send custom data, code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
await currentAVSession.sendCustomData({customData : "This is custom data"}).then(() => {
  console.info('Succeeded in sending custom data.');
});
```

```TypeScript
// Index.ets
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;

  aboutToAppear(): void {
    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(`Succeeded in creating AV session, sessionId: ${this.sessionId}`);
        (this.controller as avSession.AVSessionController).sendCustomData({ customData: "This is my data" });
      });
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## setAVCallState

```TypeScript
setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void
```

设置通话状态。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void--><!--Device-AVSession-setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVCallState](arkts-avsession-avsession-avcallstate-i.md) | 是 | 通话状态。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
let calldata: avSession.AVCallState = {
  state: avSession.CallState.CALL_STATE_ACTIVE,
  muted: false
};
currentAVSession.setAVCallState(calldata).then(() => {
  console.info('Succeeded in setting AVCallState.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avcalldata: avSession.AVCallState = {
  state: avSession.CallState.CALL_STATE_ACTIVE,
  muted: false
};
currentAVSession.setAVCallState(avcalldata, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set AVCallState, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting AVCallState.');
});
```

## setAVCallState

```TypeScript
setAVCallState(state: AVCallState): Promise<void>
```

设置通话状态。结果通过Promise异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-setAVCallState(state: AVCallState): Promise<void>--><!--Device-AVSession-setAVCallState(state: AVCallState): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVCallState](arkts-avsession-avsession-avcallstate-i.md) | 是 | 通话状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setAVCallState](#setavcallstate)

## setAVMetadata

```TypeScript
setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void
```

设置会话元数据。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void--><!--Device-AVSession-setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | AVMetadata | 是 | 会话元数据。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
let metadata: avSession.AVMetadata = {
  assetId: "121278",
  title: "lose yourself",
  artist: "Eminem",
  author: "ST",
  album: "Slim shady",
  writer: "ST",
  composer: "ST",
  duration: 2222,
  mediaImage: "https://www.example.com/example.jpg",
  subtitle: "8 Mile",
  description: "Rap",
  // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
  // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
  lyric: "lrc格式歌词内容",
  // singleLyricText字段存储单条歌词文本，不包含时间戳。
  // 例如："单条歌词内容"。
  singleLyricText: "单条歌词内容",
  previousAssetId: "121277",
  nextAssetId: "121279"
};
currentAVSession.setAVMetadata(metadata).then(() => {
  console.info('Succeeded in setting AVMetadata.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let metadata: avSession.AVMetadata = {
  assetId: "121278",
  title: "lose yourself",
  artist: "Eminem",
  author: "ST",
  album: "Slim shady",
  writer: "ST",
  composer: "ST",
  duration: 2222,
  mediaImage: "https://www.example.com/example.jpg",
  subtitle: "8 Mile",
  description: "Rap",
  // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
  // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
  lyric: "lrc格式歌词内容",
  // singleLyricText字段存储单条歌词文本，不包含时间戳。
  // 例如："单条歌词内容"。
  singleLyricText: "单条歌词内容",
  previousAssetId: "121277",
  nextAssetId: "121279"
};
currentAVSession.setAVMetadata(metadata, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set AVMetadata, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting AVMetadata.');
});
```

## setAVMetadata

```TypeScript
setAVMetadata(data: AVMetadata): Promise<void>
```

设置会话元数据。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setAVMetadata(data: AVMetadata): Promise<void>--><!--Device-AVSession-setAVMetadata(data: AVMetadata): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | AVMetadata | 是 | 会话元数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setAVMetadata](#setavmetadata)

## setAVPlaybackState

```TypeScript
setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void
```

设置会话播放状态。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void--><!--Device-AVSession-setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md) | 是 | 会话播放状态，包括状态、倍数、循环模式等信息。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
let playbackState: avSession.AVPlaybackState = {
  state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
  speed: 1.0,
  position:{elapsedTime:10, updateTime:(new Date()).getTime()},
  bufferedTime:1000,
  loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
  isFavorite:true
};
currentAVSession.setAVPlaybackState(playbackState).then(() => {
  console.info('Succeeded in setting AVPlaybackState.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let playbackState: avSession.AVPlaybackState = {
  state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
  speed: 1.0,
  position:{elapsedTime:10, updateTime:(new Date()).getTime()},
  bufferedTime:1000,
  loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
  isFavorite:true
};
currentAVSession.setAVPlaybackState(playbackState, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set AVPlaybackState, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting AVPlaybackState.');
});
```

## setAVPlaybackState

```TypeScript
setAVPlaybackState(state: AVPlaybackState): Promise<void>
```

设置会话播放状态。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setAVPlaybackState(state: AVPlaybackState): Promise<void>--><!--Device-AVSession-setAVPlaybackState(state: AVPlaybackState): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md) | 是 | 会话播放状态，包括状态、倍数、循环模式等信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当播放状态设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setAVPlaybackState](#setavplaybackstate)

## setAVQueueItems

```TypeScript
setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void
```

设置媒体播放列表。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void--><!--Device-AVSession-setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | 是 | 播放列表单项的队列，用以表示播放列表。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
// Index.ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
let imageSource = await image.createImageSource(value.buffer);
let imagePixel = await imageSource.createPixelMap({desiredSize:{width: 150, height: 150}});
let queueItemDescription_1: avSession.AVMediaDescription = {
  assetId: '001',
  title: 'music_name',
  subtitle: 'music_sub_name',
  description: 'music_description',
  mediaImage : imagePixel,
  extras: {extras:'any'}
};
let queueItem_1: avSession.AVQueueItem = {
  itemId: 1,
  description: queueItemDescription_1
} as avSession.AVQueueItem;
let queueItemDescription_2: avSession.AVMediaDescription = {
  assetId: '002',
  title: 'music_name',
  subtitle: 'music_sub_name',
  description: 'music_description',
  mediaImage: imagePixel,
  extras: {extras:'any'}
};
let queueItem_2: avSession.AVQueueItem = {
  itemId: 2,
  description: queueItemDescription_2
} as avSession.AVQueueItem;
let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
currentAVSession.setAVQueueItems(queueItemsArray).then(() => {
  console.info('Succeeded in setting AVQueueItems.');
});
```

```TypeScript
// Index.ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
let imageSource = await image.createImageSource(value.buffer);
let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
let queueItemDescription_1: avSession.AVMediaDescription = {
  assetId: '001',
  title: 'music_name',
  subtitle: 'music_sub_name',
  description: 'music_description',
  mediaImage: imagePixel,
  extras: { extras: 'any' }
};
let queueItem_1: avSession.AVQueueItem = {
  itemId: 1,
  description: queueItemDescription_1
};
let queueItemDescription_2: avSession.AVMediaDescription = {
  assetId: '002',
  title: 'music_name',
  subtitle: 'music_sub_name',
  description: 'music_description',
  mediaImage: imagePixel,
  extras: { extras: 'any' }
};
let queueItem_2: avSession.AVQueueItem = {
  itemId: 2,
  description: queueItemDescription_2
};
let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
currentAVSession.setAVQueueItems(queueItemsArray, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set AVQueueItems, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting AVQueueItems.');
});
```

## setAVQueueItems

```TypeScript
setAVQueueItems(items: Array<AVQueueItem>): Promise<void>
```

设置媒体播放列表。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setAVQueueItems(items: Array<AVQueueItem>): Promise<void>--><!--Device-AVSession-setAVQueueItems(items: Array<AVQueueItem>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | 是 | 播放列表单项的队列，用以表示播放列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setAVQueueItems](#setavqueueitems)

## setAVQueueTitle

```TypeScript
setAVQueueTitle(title: string, callback: AsyncCallback<void>): void
```

设置媒体播放列表名称。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-setAVQueueTitle(title: string, callback: AsyncCallback<void>): void--><!--Device-AVSession-setAVQueueTitle(title: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 播放列表名称字段。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
let queueTitle = 'QUEUE_TITLE';
currentAVSession.setAVQueueTitle(queueTitle).then(() => {
  console.info('Succeeded in setting AVQueueTitle.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let queueTitle = 'QUEUE_TITLE';
currentAVSession.setAVQueueTitle(queueTitle, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set AVQueueTitle, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting AVQueueTitle.');
});
```

## setAVQueueTitle

```TypeScript
setAVQueueTitle(title: string): Promise<void>
```

设置媒体播放列表名称。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setAVQueueTitle(title: string): Promise<void>--><!--Device-AVSession-setAVQueueTitle(title: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 播放列表的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setAVQueueTitle](#setavqueuetitle)

## setBackgroundPlayMode

```TypeScript
setBackgroundPlayMode(mode: BackgroundPlayMode): Promise<void>
```

设置后台播放模式。使用promise异步回调。建议与应用内"是否支持后台播放开关"关联。如未设置，'audio'类型会话默认值为ENABLE_BACKGROUND_PLAY；'video'类型会话默认值为DISABLE_BACKGROUND_PLAY。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-setBackgroundPlayMode(mode: BackgroundPlayMode): Promise<void>--><!--Device-AVSession-setBackgroundPlayMode(mode: BackgroundPlayMode): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [BackgroundPlayMode](arkts-avsession-avsession-backgroundplaymode-e.md) | 是 | 后台播放模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
try {
  currentAVSession.setBackgroundPlayMode(avSession.BackgroundPlayMode.ENABLE_BACKGROUND_PLAY);
} catch (err) {
  console.error(`setBackgroundPlayMode BusinessError: code: ${err.code}, message: ${err.message}`);
}
```

## setCallMetadata

```TypeScript
setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void
```

设置通话会话元数据。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void--><!--Device-AVSession-setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [CallMetadata](arkts-avsession-avsession-callmetadata-i.md) | 是 | 通话会话元数据。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
// Index.ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { avSession } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height('100%')
  }
}

class CallManager {
  private currentAVSession: avSession.AVSession | null = null;

  async setCallMetadata() {
    let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
    let imageSource = await image.createImageSource(value.buffer);
    let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
    let calldata: avSession.CallMetadata = {
      name: "xiaoming",
      phoneNumber: "111xxxxxxxx",
      avatar: imagePixel
    };
    this.currentAVSession?.setCallMetadata(calldata).then(() => {
      console.info('Succeeded in setting call metadata.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to set call metadata, code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

```TypeScript
// Index.ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height('100%')
  }
}

class CallManager {
  private currentAVSession: avSession.AVSession | null = null;

  async setCallMetadata() {
    let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
    let imageSource = await image.createImageSource(value.buffer);
    let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
    let calldata: avSession.CallMetadata = {
      name: "xiaoming",
      phoneNumber: "111xxxxxxxx",
      avatar: imagePixel
    };
    this.currentAVSession?.setCallMetadata(calldata, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to set call metadata, code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('Succeeded in setting call metadata.');
    });
  }
}
```

## setCallMetadata

```TypeScript
setCallMetadata(data: CallMetadata): Promise<void>
```

设置通话会话元数据。结果通过Promise异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-setCallMetadata(data: CallMetadata): Promise<void>--><!--Device-AVSession-setCallMetadata(data: CallMetadata): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [CallMetadata](arkts-avsession-avsession-callmetadata-i.md) | 是 | 通话会话元数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setCallMetadata](#setcallmetadata)

## setDesktopLyricState

```TypeScript
setDesktopLyricState(state: DesktopLyricState): Promise<void>
```

设置当前会话桌面歌词状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-setDesktopLyricState(state: DesktopLyricState): Promise<void>--><!--Device-AVSession-setDesktopLyricState(state: DesktopLyricState): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md) | 是 | 桌面歌词状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |
| [6600110](../errorcode-avsession.md#6600110-应用程序的桌面歌词功能未开启) | The desktop lyrics feature of this application is not enabled. |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) | The desktop lyrics feature is not supported. |

**示例**

```TypeScript
let state: avSession.DesktopLyricState = {
  isLocked: true,
};
currentAVSession.setDesktopLyricState(state).then(() => {
  console.info('setDesktopLyricState successfully');
});
```

```TypeScript
let state: avSession.DesktopLyricState = {
  isLocked: true,
};
currentAVSession.setDesktopLyricState(state).then(() => {
  console.info('setDesktopLyricState successfully');
});
```

```TypeScript
let state: avSession.DesktopLyricState = {
  isLocked: true,
};
avcontroller.setDesktopLyricState(state);
```

## setDesktopLyricVisible

```TypeScript
setDesktopLyricVisible(visible: boolean): Promise<void>
```

设置当前会话桌面歌词的显示状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-setDesktopLyricVisible(visible: boolean): Promise<void>--><!--Device-AVSession-setDesktopLyricVisible(visible: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 是否显示桌面歌词。true表示显示；false表示不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |
| [6600110](../errorcode-avsession.md#6600110-应用程序的桌面歌词功能未开启) | The desktop lyrics feature of this application is not enabled. |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) | The desktop lyrics feature is not supported. |

**示例**

```TypeScript
currentAVSession.setDesktopLyricVisible(true).then(() => {
  console.info('Succeeded in setting desktop lyric visible.');
});
```

```TypeScript
currentAVSession.setDesktopLyricVisible(true).then(() => {
  console.info('Succeeded in setting desktop lyric visible.');
});
```

```TypeScript
avcontroller.setDesktopLyricVisible(true);
```

## setExtras

```TypeScript
setExtras(extras: {[key: string]: Object}, callback: AsyncCallback<void>): void
```

媒体提供方设置键值对形式的自定义媒体数据包，使用callback异步回调。

**起始版本：** 10

<!--Device-AVSession-setExtras(extras: {[key: string]: Object}, callback: AsyncCallback<void>): void--><!--Device-AVSession-setExtras(extras: {[key: string]: Object}, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | {[key: string]: Object} | 是 | 需要传递的自定义媒体数据包键值对。 <br> **说明：** 参数extras支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见 [@ohos.app.ability.Want (Want)](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当自定义媒体数据包设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
currentAVSession.setExtras({extras : "This is custom media packet"}).then(() => {
  console.info('Succeeded in setting extras.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.setExtras({extras : "This is custom media packet"}, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set extras, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting extras.');
})
```

## setExtras

```TypeScript
setExtras(extras: Record<string, Object>, callback: AsyncCallback<void>): void
```

Set the custom media packets for this session.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-setExtras(extras: Record<string, Object>, callback: AsyncCallback<void>): void--><!--Device-AVSession-setExtras(extras: Record<string, Object>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | Record&lt;string, Object&gt; | 是 | The custom media packets <br>设置的应用自定义扩展参数 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The asyncCallback triggered when the command is executed successfully. <br>回调返回 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setExtras](#setextras)

## setExtras

```TypeScript
setExtras(extras: {[key: string]: Object}): Promise<void>
```

媒体提供方设置键值对形式的自定义媒体数据包。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setExtras(extras: {[key: string]: Object}): Promise<void>--><!--Device-AVSession-setExtras(extras: {[key: string]: Object}): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | {[key: string]: Object} | 是 | 需要传递的自定义媒体数据包键值对。 <br> **说明：** 参数extras支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见 [@ohos.app.ability.Want (Want)](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setExtras](#setextras)

## setExtras

```TypeScript
setExtras(extras: Record<string, Object>): Promise<void>
```

Set the custom media packets for this session.

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setExtras(extras: Record<string, Object>): Promise<void>--><!--Device-AVSession-setExtras(extras: Record<string, Object>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | Record&lt;string, Object&gt; | 是 | The custom media packets |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setExtras](#setextras)

## setLaunchAbility

```TypeScript
setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void
```

设置一个WantAgent用于拉起会话的Ability。结果通过callback异步回调方式返回。通过点击播控组件可以跳转到对应的播放界面，默认跳转到[avSession.createAVSession](arkts-avsession-avsession-createavsession-f.md)接口传入的context所属的UIAbility界面。

**起始版本：** 23

<!--Device-AVSession-setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void--><!--Device-AVSession-setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md) | 是 | 应用的相关属性信息，如bundleName，abilityName，deviceId等。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当Ability设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
import { wantAgent } from '@kit.AbilityKit';

// WantAgentInfo对象。
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: "deviceId",
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility",
      action: "action1",
      entities: ["entity1"],
      type: "MIMETYPE",
      uri: "key = {true,true,false}",
      parameters:
        {
          mykey0: 2222,
          mykey1: [1, 2, 3],
          mykey2: "[1, 2, 3]",
          mykey3: "ssssssssssssssssssssssssss",
          mykey4: [false, true, false],
          mykey5: ["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"],
          mykey6: true
        }
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
  wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
}

wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
  currentAVSession.setLaunchAbility(agent).then(() => {
    console.info('Succeeded in setting launch ability.');
  });
});
```

```TypeScript
import { wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// WantAgentInfo对象。
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: "deviceId",
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility",
      action: "action1",
      entities: ["entity1"],
      type: "MIMETYPE",
      uri: "key = {true,true,false}",
      parameters:
        {
          mykey0: 2222,
          mykey1: [1, 2, 3],
          mykey2: "[1, 2, 3]",
          mykey3: "ssssssssssssssssssssssssss",
          mykey4: [false, true, false],
          mykey5: ["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"],
          mykey6: true
        }
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
  wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
}

wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
  currentAVSession.setLaunchAbility(agent, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set launch ability, code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in setting launch ability.');
  });
});
```

## setLaunchAbility

```TypeScript
setLaunchAbility(ability: WantAgent): Promise<void>
```

设置一个WantAgent用于拉起会话的Ability。结果通过Promise异步回调方式返回。通过点击播控组件可以跳转到对应的播放界面，默认跳转到[avSession.createAVSession](arkts-avsession-avsession-createavsession-f.md)接口传入的context所属的UIAbility界面。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setLaunchAbility(ability: WantAgent): Promise<void>--><!--Device-AVSession-setLaunchAbility(ability: WantAgent): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md) | 是 | 应用的相关属性信息，如bundleName，abilityName，deviceId等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当Ability设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

参见 [setLaunchAbility](#setlaunchability)

## setMediaCenterControlType

```TypeScript
setMediaCenterControlType(type: Array<AVMediaCenterControlType>): Promise<void>
```

设置应用支持的控制类型列表。使用Promise异步回调。设置优先显示在播控中心的控制类型列表，若未设置控制类型优先级，播控中心将根据[AVSessionType](arkts-avsession-avsession-avsessiontype-t.md)显示，具体显示规则参考 [创建不同类型的会话](../../../media/avsession/avsession-access-scene.md#创建不同类型的会话)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSession-setMediaCenterControlType(type: Array<AVMediaCenterControlType>): Promise<void>--><!--Device-AVSession-setMediaCenterControlType(type: Array<AVMediaCenterControlType>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | Array&lt;[AVMediaCenterControlType](arkts-avsession-avsession-avmediacentercontroltype-t.md)&gt; | 是 | 优先在播控中心显示的控制类型列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
try {
  let controlTypes: avSession.AVMediaCenterControlType[] = [
    'playNext',
    'playPrevious',
    'setSpeed',
    'setLoopMode'
  ];
  await currentAVSession.setMediaCenterControlType(controlTypes);
  console.info('Succeeded in setting media center control type.');
} catch (err) {
  console.error(`setMediaCenterControlType BusinessError: code: ${err.code}, message: ${err.message}`);
}
```

## setSupportedLoopModes

```TypeScript
setSupportedLoopModes(loopModes: Array<LoopMode>): Promise<void>
```

设置应用支持的循环模式列表。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setSupportedLoopModes(loopModes: Array<LoopMode>): Promise<void>--><!--Device-AVSession-setSupportedLoopModes(loopModes: Array<LoopMode>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loopModes | Array&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt; | 是 | 支持的循环模式列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
try {
  let loopModes: avSession.LoopMode[] = [
    avSession.LoopMode.LOOP_MODE_SEQUENCE,
    avSession.LoopMode.LOOP_MODE_SINGLE,
    avSession.LoopMode.LOOP_MODE_LIST
  ];
  await currentAVSession.setSupportedLoopModes(loopModes);
  console.info('Succeeded in setting supported loop modes.');
} catch (err) {
  console.error(`setSupportedLoopModes BusinessError: code: ${err.code}, message: ${err.message}`);
}
```

## setSupportedPlaySpeeds

```TypeScript
setSupportedPlaySpeeds(speeds: Array<double>): Promise<void>
```

设置应用支持的播放倍速列表。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-setSupportedPlaySpeeds(speeds: Array<double>): Promise<void>--><!--Device-AVSession-setSupportedPlaySpeeds(speeds: Array<double>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speeds | Array&lt;double&gt; | 是 | 支持的播放倍速列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) | Session service exception |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) | The session does not exist. |

**示例**

```TypeScript
try {
  let speeds: double[] = [0.5, 1, 1.25, 1.5];
  await currentAVSession.setSupportedPlaySpeeds(speeds);
  console.info('Succeeded in setting supported play speeds.');
} catch (err) {
  console.error(`setSupportedPlaySpeeds BusinessError: code: ${err.code}, message: ${err.message}`);
}
```

## stopCasting

```TypeScript
stopCasting(callback: AsyncCallback<void>): void
```

结束投播。结果通过callback异步回调方式返回。

**起始版本：** 23

<!--Device-AVSession-stopCasting(callback: AsyncCallback<void>): void--><!--Device-AVSession-stopCasting(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) | The remote connection is not established |

**示例**

```TypeScript
currentAVSession.stopCasting(() => {
  console.info('Succeeded in stopping casting.');
});
```

```TypeScript
currentAVSession.stopCasting().then(() => {
  console.info('Succeeded in stopping casting.');
});
```

```TypeScript
let sessionId = 'xxx'; // sessionId需要通过avSession.createAVSession创建会话后获取。
let myToken: avSession.SessionToken = {
  sessionId: sessionId,
}
avSession.stopCasting(myToken, () => {
    console.info('Succeeded in stopping casting.');
});
```

```TypeScript
let sessionId = 'xxx'; // sessionId需要通过avSession.createAVSession创建会话后获取。
let myToken: avSession.SessionToken = {
  sessionId: sessionId,
}
avSession.stopCasting(myToken).then(() => {
  console.info('stopCasting successfully');
});
```

## stopCasting

```TypeScript
stopCasting(): Promise<void>
```

结束投播。结果通过Promise异步回调方式返回。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-stopCasting(): Promise<void>--><!--Device-AVSession-stopCasting(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当成功结束投播，无返回结果，否则返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) | The remote connection is not established |

**示例**

参见 [stopCasting](#stopcasting)

## sessionId

```TypeScript
readonly sessionId: string
```

AVSession对象唯一的会话标识。

**类型：** string

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-readonly sessionId: string--><!--Device-AVSession-readonly sessionId: string-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

## sessionTag

```TypeScript
readonly sessionTag: string
```

AVSession会话的自定义标签信息。

**类型：** string

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-readonly sessionTag: string--><!--Device-AVSession-readonly sessionTag: string-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

## sessionType

```TypeScript
readonly sessionType: AVSessionType
```

AVSession会话类型。

**类型：** [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md)

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSession-readonly sessionType: AVSessionType--><!--Device-AVSession-readonly sessionType: AVSessionType-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

