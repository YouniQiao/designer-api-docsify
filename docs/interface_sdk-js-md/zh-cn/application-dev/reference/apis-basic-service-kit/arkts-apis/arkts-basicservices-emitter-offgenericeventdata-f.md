# offGenericEventData

## 导入模块

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## offGenericEventData

```TypeScript
function offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

取消订阅当前Emitter类实例的事件。仅当已使用  
[onGenericEventData](emitter.onGenericEventData&lt;T&gt;(eventId: string, callback: Callback&lt;GenericEventData<T>&gt;&lt;T&gt;>))或  
[onceGenericEventData](emitter.onceGenericEventData&lt;T&gt;(eventId: string, callback: Callback&lt;GenericEventData<T>&gt;&lt;T&gt;>))接口订阅了事件ID为eventId且回调处理函数为callback的事件时，该接口才生效。

使用该接口取消事件订阅后，已通过[emit](emitter.emit(eventId: string))接口发布但尚未执行的事件将被取消。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-emitter-function offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | 是 | 事件的回调处理函数。 |

