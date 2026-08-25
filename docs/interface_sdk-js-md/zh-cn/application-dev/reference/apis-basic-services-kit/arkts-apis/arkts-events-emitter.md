# @ohos.events.emitter(Emitter)

本模块提供进程内线程间或线程内事件的发送与处理能力。开发者可以使用本模块的 API，订阅事件（持续订阅或 单次订阅）、取消订阅事件，发送事件到事件队列中，以及查询事件的订阅数量，从而实现同一进程内不同线程之 间、以及同一线程内的事件通信。适用于跨线程通信、模块解耦、事件驱动等场景，能够帮助开发者实现轻量级 的发布-订阅模式，降低组件间的耦合度，提升代码的可维护性和可扩展性。提供两种事件处理入口，开发者可根据隔离需求选择：  
- **命名空间级 API**（`emitter` 命名空间下的 `on`、`once`、`off`、`emit`、`getListenerCount` 等函 数）：提供进程内全局范围的事件订阅与发布能力。该入口基于全局事件队列工作，同进程内任意线程均可订阅和 发布事件，适用于跨线程事件通信。 - **实例级 API**（`Emitter` 类）：提供同一 `Emitter` 实例范围内的事件订阅与发布能力。不同 `Emitter` 实例之间相互隔离，开发者可创建多个独立的事件通信通道，适用于需要事件隔离或按实例分组的 场景。  
**API 组合使用关系说明：**本模块的事件通信遵循"订阅 → 发布 → 处理 → 取消订阅"的组合调用模式。无论是命名空间级 API 还是实例 级 API，均需先订阅事件，再由其他线程或同一线程发布事件，收到事件后执行回调处理；当不再需要接收事件 时，应取消订阅以释放资源。同时，事件订阅具有明确的生命周期，开发者应注意资源管理： - **持续订阅**（`on`）：订阅后持续有效，直至调用 `off` 取消订阅。若未取消，订阅将一直保留。 - **单次订阅**（`once`）：订阅后，仅在首次接收到事件并执行回调后自动取消，无需手动调用 `off`。 - **取消订阅的时机**：调用 `off` 取消订阅后，已通过 `emit` 发布但尚未执行的事件也将被取消，不再 触发回调。同时需要注意，取消指定回调时，需传入对应的 `callback` 函数；若未指定，表示取消该事件的所有 订阅。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.Emitter

## 导入模块

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [emit(Emitter)](arkts-basicservices-emitter-emit-f.md) |
| [getListenerCount(Emitter)](arkts-basicservices-emitter-getlistenercount-f.md) |
| [off(Emitter)](arkts-basicservices-emitter-off-f.md) |
| [off(Emitter)](arkts-basicservices-emitter-off-f.md) |
| [off(Emitter)](arkts-basicservices-emitter-off-f.md) |
| [off(Emitter)](arkts-basicservices-emitter-off-f.md) |
| [off(Emitter)](arkts-basicservices-emitter-off-f.md) |
| [offEventData(Emitter)](arkts-basicservices-emitter-offeventdata-f.md) |
| [offGenericEventData(Emitter)](arkts-basicservices-emitter-offgenericeventdata-f.md) |
| [on(Emitter)](arkts-basicservices-emitter-on-f.md) |
| [on(Emitter)](arkts-basicservices-emitter-on-f.md) |
| [on(Emitter)](arkts-basicservices-emitter-on-f.md) |
| [once(Emitter)](arkts-basicservices-emitter-once-f.md) |
| [once(Emitter)](arkts-basicservices-emitter-once-f.md) |
| [once(Emitter)](arkts-basicservices-emitter-once-f.md) |
| [onceEventData(Emitter)](arkts-basicservices-emitter-onceeventdata-f.md) |
| [onceGenericEventData(Emitter)](arkts-basicservices-emitter-oncegenericeventdata-f.md) |
| [onEventData(Emitter)](arkts-basicservices-emitter-oneventdata-f.md) |
| [onGenericEventData(Emitter)](arkts-basicservices-emitter-ongenericeventdata-f.md) |

### 类

| 名称 |
| --- |
| [Emitter(Emitter)](arkts-basicservices-emitter-emitter-c.md) |

### 接口

| 名称 |
| --- |
| [EventData(Emitter)](arkts-basicservices-emitter-eventdata-i.md) |
| [GenericEventData(Emitter)](arkts-basicservices-emitter-genericeventdata-i.md) |
| [InnerEvent(Emitter)](arkts-basicservices-emitter-innerevent-i.md) |
| [Options(Emitter)](arkts-basicservices-emitter-options-i.md) |

### 枚举

| 名称 |
| --- |
| [EventPriority(Emitter)](arkts-basicservices-emitter-eventpriority-e.md) |
