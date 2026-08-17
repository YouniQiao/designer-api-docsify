# CustomComponentLifecycle

**CustomComponentLifecycle** monitors the lifecycle changes of a custom component.

**Since:** 23

<!--Device-unnamed-export declare interface CustomComponentLifecycle--><!--Device-unnamed-export declare interface CustomComponentLifecycle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2 } from 'AppStorageV2';
import { PersistenceV2 } from 'PersistenceV2';
import { Type } from 'Type';
import { UIUtils } from 'UIUtils';
import { ConnectOptions } from 'ConnectOptions';
import { Binding } from 'Binding';
import { MutableBinding } from 'MutableBinding';
import { CustomComponentLifecycle } from 'CustomComponentLifecycle';
import { CustomComponentLifecycleObserver } from 'CustomComponentLifecycleObserver';
import { CustomComponentLifecycleState } from 'CustomComponentLifecycleState';
import { ComponentInit } from 'ComponentInit';
import { ComponentAppear } from 'ComponentAppear';
import { ComponentBuilt } from 'ComponentBuilt';
import { ComponentReuse } from 'ComponentReuse';
import { ComponentActive } from 'ComponentActive';
import { ComponentInactive } from 'ComponentInactive';
import { ComponentRecycle } from 'ComponentRecycle';
import { ComponentDisappear } from 'ComponentDisappear';
import { CollectionType } from 'CollectionType';
import { ConnectOptionsCollections } from 'ConnectOptionsCollections';
import { CustomComponentContext } from 'CustomComponentContext';
import { IReusePool } from 'IReusePool';
import { IReusableInfo } from 'IReusableInfo';
```

## addObserver

```TypeScript
addObserver(observer: CustomComponentLifecycleObserver): void
```

Registers a listener for the lifecycle of a custom component. Lifecycle changes will trigger the lifecycle callback in the listener.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CustomComponentLifecycle-addObserver(observer: CustomComponentLifecycleObserver): void--><!--Device-CustomComponentLifecycle-addObserver(observer: CustomComponentLifecycleObserver): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [CustomComponentLifecycleObserver](arkts-arkui-arkui-statemanagement-customcomponentlifecycleobserver-i.md) | Yes | Listener for a custom component. |

## getCurrentState

```TypeScript
getCurrentState(): CustomComponentLifecycleState
```

getCurrentState(): CustomComponentLifecycleState

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CustomComponentLifecycle-getCurrentState(): CustomComponentLifecycleState--><!--Device-CustomComponentLifecycle-getCurrentState(): CustomComponentLifecycleState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CustomComponentLifecycleState](arkts-arkui-arkui-statemanagement-customcomponentlifecyclestate-e.md) | Current lifecycle status of a custom component. |

## removeObserver

```TypeScript
removeObserver(observer: CustomComponentLifecycleObserver): void
```

Removes a listener for the lifecycle of a custom component. After the listener is removed, the lifecycle callback in the listener is not triggered even if the component status changes.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CustomComponentLifecycle-removeObserver(observer: CustomComponentLifecycleObserver): void--><!--Device-CustomComponentLifecycle-removeObserver(observer: CustomComponentLifecycleObserver): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [CustomComponentLifecycleObserver](arkts-arkui-arkui-statemanagement-customcomponentlifecycleobserver-i.md) | Yes | Listener for a custom component. |

