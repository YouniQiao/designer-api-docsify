# InteractionEventBindingInfo

组件的交互事件绑定状态信息。如果当前节点上绑定了所要查询的交互事件，调用查询接口时返回一个InteractionEventBindingInfo对象，指示事件绑定详细信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface InteractionEventBindingInfo--><!--Device-unnamed-export declare interface InteractionEventBindingInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## baseEventRegistered

```TypeScript
baseEventRegistered: boolean
```

是否以声明方式绑定事件。

true表示以声明方式绑定事件，false表示没有以声明方式绑定事件。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionEventBindingInfo-baseEventRegistered: boolean--><!--Device-InteractionEventBindingInfo-baseEventRegistered: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builtInEventRegistered

```TypeScript
builtInEventRegistered: boolean
```

组件是否绑定内置事件(组件内部定义的事件, 无需开发者手动绑定)。

true表示组件绑定内置事件，false表示组件没有绑定内置事件。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionEventBindingInfo-builtInEventRegistered: boolean--><!--Device-InteractionEventBindingInfo-builtInEventRegistered: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## nativeEventRegistered

```TypeScript
nativeEventRegistered: boolean
```

是否以注册节点事件（  
[registerNodeEvent](../../../reference/apis-arkui/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)）的方式绑定事件。

true表示以注册节点事件的方式绑定事件，false表示没有以注册节点事件的方式绑定事件。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionEventBindingInfo-nativeEventRegistered: boolean--><!--Device-InteractionEventBindingInfo-nativeEventRegistered: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## nodeEventRegistered

```TypeScript
nodeEventRegistered: boolean
```

是否以自定义组件节点的方式绑定事件，请参考[基础事件示例](../../../reference/apis-arkui/js-apis-arkui-frameNode-static.md#基础事件示例)

true表示以自定义组件节点的方式绑定事件，false表示没有以自定义组件节点的方式绑定事件。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionEventBindingInfo-nodeEventRegistered: boolean--><!--Device-InteractionEventBindingInfo-nodeEventRegistered: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

