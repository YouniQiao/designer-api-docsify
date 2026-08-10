# EntryOptions

页面入口配置选项，用于在\@Entry装饰页面时配置路由名称、状态存储和共享存储等参数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface EntryOptions--><!--Device-unnamed-declare interface EntryOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## routeName

```TypeScript
routeName? : string
```

表示作为命名路由页面的名称。当需要通过命名路由方式跳转到此页面时，需设置此参数作为路由名称。不传入时，该页面不会注册为命名路由页面，无法通过命名路由方式跳转访问，仅作为默认入口页面加载。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-EntryOptions-routeName? : string--><!--Device-EntryOptions-routeName? : string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## storage

```TypeScript
storage? : LocalStorage
```

页面级的UI状态存储。当需要在页面外部预先创建并管理UI状态、或需要将已有的LocalStorage实例绑定到此页面以实现状态共享时，传入此参数。当未传入时，框架会创建一个新的LocalStorage实例作为默认值。当useSharedStorage设置为true且storage已赋值时，useSharedStorage的值优先级更高。

**Type:** [LocalStorage](../arkts-apis/arkts-arkui-localstorage-localstorage-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-EntryOptions-storage? : LocalStorage--><!--Device-EntryOptions-storage? : LocalStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useSharedStorage

```TypeScript
useSharedStorage? : boolean
```

是否使用  
[loadContent](../arkts-apis/arkts-arkui-window-windowstage-i.md/arkts-arkui-window-windowstage-i.md#loadcontent)传入的LocalStorage实例。默认值false。true：使用共享的LocalStorage实例（前提条件：需确保loadContent接口已传入LocalStorage实例；若未传入，则创建新的LocalStorage实例）。false：不使用共享的LocalStorage实例。当useSharedStorage设置为true且storage已赋值时，useSharedStorage的值优先级更高。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-EntryOptions-useSharedStorage? : boolean--><!--Device-EntryOptions-useSharedStorage? : boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

