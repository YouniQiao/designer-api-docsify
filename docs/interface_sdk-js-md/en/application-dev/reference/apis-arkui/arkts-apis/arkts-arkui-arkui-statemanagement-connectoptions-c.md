# ConnectOptions

Defines the parameter type for **globalConnect**.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export class ConnectOptions--><!--Device-unnamed-export class ConnectOptions-End-->

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

## areaMode

```TypeScript
areaMode?: contextConstant.AreaMode
```

Encryption level, ranging from EL1 to EL5 (corresponding to the value from 0 to 4). For details, see [Encryption Levels](../../../application-models/application-context-stage.md#obtaining-and-modifying-encryption-levels). If no value is passed in, EL2 is used by default. Storage paths vary based on the encryption levels. If the input value of encryption level is not in the range of **0** to **4**, a crash occurs.

**Type:** contextConstant.AreaMode

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConnectOptions-areaMode?: contextConstant.AreaMode--><!--Device-ConnectOptions-areaMode?: contextConstant.AreaMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultCreator

```TypeScript
defaultCreator?: StorageDefaultCreator<T>
```

Default constructor. You are advised to pass this parameter. If **globalConnect** is connected to the key for the first time, an error is reported if this parameter is not passed in.

**Type:** [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConnectOptions-defaultCreator?: StorageDefaultCreator<T>--><!--Device-ConnectOptions-defaultCreator?: StorageDefaultCreator<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string
```

Input key. If no value is passed in, the type name is used as the key.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConnectOptions-key?: string--><!--Device-ConnectOptions-key?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: TypeConstructorWithArgs<T>
```

Specified type.

**Type:** [TypeConstructorWithArgs](arkts-arkui-arkui-statemanagement-typeconstructorwithargs-i.md)&lt;T&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ConnectOptions-type: TypeConstructorWithArgs<T>--><!--Device-ConnectOptions-type: TypeConstructorWithArgs<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

