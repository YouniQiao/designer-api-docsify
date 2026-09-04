# UIContext

```TypeScript
declare type UIContext = import('../api/@ohos.arkui.UIContext').UIContext
```

UIContext

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Type:** import('../api/@ohos.arkui.UIContext').UIContext

**Examples**

```TypeScript
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct MyComponent {
  aboutToAppear() {
    let uiContext: UIContext = this.getUIContext();
  }

  build() {
    // ...
  }
}
```
