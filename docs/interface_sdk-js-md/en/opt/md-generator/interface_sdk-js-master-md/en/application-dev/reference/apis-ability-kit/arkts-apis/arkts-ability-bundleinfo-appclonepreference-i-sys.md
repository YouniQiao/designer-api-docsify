# AppClonePreference (System API)

Defines the application clone preference configuration.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-unnamed-export interface AppClonePreference--><!--Device-unnamed-export interface AppClonePreference-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## appIndex

```TypeScript
appIndex?: number
```

Index of the application clone. This value is valid only when the mode is CLONE_APP. The value ranges from 1 to 5 (maximum 5 clones are supported). The value should be an integer.

**Type:** number

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppClonePreference-appIndex?: int--><!--Device-AppClonePreference-appIndex?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## mode

```TypeScript
mode: bundleManager.AppClonePreferenceMode
```

Preference mode for application cloning.

**Type:** bundleManager.AppClonePreferenceMode

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppClonePreference-mode: bundleManager.AppClonePreferenceMode--><!--Device-AppClonePreference-mode: bundleManager.AppClonePreferenceMode-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.
