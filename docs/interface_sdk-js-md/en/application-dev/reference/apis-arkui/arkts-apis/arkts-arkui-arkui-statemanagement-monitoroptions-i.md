# MonitorOptions

Defines the optional parameters for [addMonitor](arkts-arkui-arkui-statemanagement-uiutils-c.md#addmonitor), which are used to configure the callback type and whether to enable the wildcard capability.

**Since:** 20

<!--Device-unnamed-export interface MonitorOptions--><!--Device-unnamed-export interface MonitorOptions-End-->

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

## enableWildcard

```TypeScript
enableWildcard?: boolean
```

Whether to enable the wildcard capability for this **addMonitor**. **true** to enable the wildcard capability, and **false** means the opposite. The default value is **false**. If the wildcard capability is disabled but the path contains wildcards, the path is considered invalid.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MonitorOptions-enableWildcard?: boolean--><!--Device-MonitorOptions-enableWildcard?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSynchronous

```TypeScript
isSynchronous?: boolean
```

Whether the current callback is a synchronous callback. **true**: The current callback is a synchronous callback. **false** (default value): The current callback is an asynchronous callback.

**Type:** boolean

**Default:** false

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-MonitorOptions-isSynchronous?: boolean--><!--Device-MonitorOptions-isSynchronous?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

