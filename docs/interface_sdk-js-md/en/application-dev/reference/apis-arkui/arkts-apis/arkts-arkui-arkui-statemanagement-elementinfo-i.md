# ElementInfo

Defines information about the components associated with the observable object, including system components and custom components.

**Since:** 23

<!--Device-unnamed-export interface ElementInfo--><!--Device-unnamed-export interface ElementInfo-End-->

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

## elementId

```TypeScript
elementId: number
```

Component ID.

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ElementInfo-elementId: number--><!--Device-ElementInfo-elementId: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## elementName

```TypeScript
elementName: string
```

Component name.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ElementInfo-elementName: string--><!--Device-ElementInfo-elementName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

