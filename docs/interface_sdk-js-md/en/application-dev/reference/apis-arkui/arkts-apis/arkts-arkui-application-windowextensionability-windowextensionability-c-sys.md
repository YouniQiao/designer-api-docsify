# WindowExtensionAbility (System API)

WindowExtensionAbility类。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 21

<!--Device-unnamed-declare class WindowExtensionAbility--><!--Device-unnamed-declare class WindowExtensionAbility-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { WindowExtensionContext } from 'kits/@kit.ArkUI';
```

## onConnect

```TypeScript
onConnect(want: Want): void
```

当窗口扩展组件第一次连接ability时回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowExtensionAbility-onConnect(want: Want): void--><!--Device-WindowExtensionAbility-onConnect(want: Want): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 当前ability的Want类型信息，包括ability名称、bundle名称等。 |

## Examples

```TypeScript
import { WindowExtensionAbility } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

export default class MyWindowExtensionAbility extends WindowExtensionAbility {
  onConnect(want: Want) {
    console.info(`WindowExtAbility onConnect, abilityName: ${want.abilityName}`);
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(want: Want): void
```

当所有连接到窗口扩展组件的ability断开连接时回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowExtensionAbility-onDisconnect(want: Want): void--><!--Device-WindowExtensionAbility-onDisconnect(want: Want): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 当前Ability的Want类型信息，包括ability名称、bundle名称等。 |

## Examples

```TypeScript
import { WindowExtensionAbility } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

export default class MyWindowExtensionAbility extends WindowExtensionAbility {
  onDisconnect(want: Want) {
    console.info(`WindowExtAbility onDisconnect, abilityName: ${want.abilityName}`);
  }
}
```

## onWindowReady

```TypeScript
onWindowReady(window: window.Window): void
```

当窗口被创建时回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowExtensionAbility-onWindowReady(window: window.Window): void--><!--Device-WindowExtensionAbility-onWindowReady(window: window.Window): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| window | window.Window | Yes | 当前窗口实例。 |

## Examples

```TypeScript
import { WindowExtensionAbility, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyWindowExtensionAbility extends WindowExtensionAbility {
  onWindowReady(window: window.Window) {
    window.setUIContent('WindowExtAbility/pages/index1',(err:BusinessError) => {
      let pro = window.getWindowProperties();
      console.info(`WindowExtension pro: ${JSON.stringify(pro)}`);
      window.showWindow();
    });
  }
}
```

## context

```TypeScript
context: WindowExtensionContext
```

Indicates window extension ability context.

**Type:** [WindowExtensionContext](arkts-arkui-windowextensioncontext-t-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowExtensionAbility-context: WindowExtensionContext--><!--Device-WindowExtensionAbility-context: WindowExtensionContext-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

