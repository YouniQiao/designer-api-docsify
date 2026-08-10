# BaseCustomComponent

基础自定义组件的定义，它是所有自定义组件的基类。

**Inheritance/Implementation:** BaseCustomComponent extends [ExtendableComponent](arkts-arkui-extendablecomponent-extendablecomponent-c.md) and implements [CommonAttribute](arkts-arkui-commonattribute-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class BaseCustomComponent<T_Options> extends ExtendableComponent implements CommonAttribute--><!--Device-unnamed-export declare abstract class BaseCustomComponent<T_Options> extends ExtendableComponent implements CommonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToRecycle

```TypeScript
aboutToRecycle(): void
```

组件复用在放入复用驰时，会触发回调

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseCustomComponent-aboutToRecycle(): void--><!--Device-BaseCustomComponent-aboutToRecycle(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

