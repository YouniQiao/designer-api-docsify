# DisposedRuleConfiguration (System API)

Describes the configurations for setting disposed rules in batches.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-appControl-export interface DisposedRuleConfiguration--><!--Device-appControl-export interface DisposedRuleConfiguration-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## appId

```TypeScript
appId: string
```

appId or appIdentifier of the target application. Identical appId and appIdentifier values indicate the same application instance. If a rule is set using appId, it overwrites the one set with appIdentifier, and the reverse is also true. **NOTE** **appId** is also the unique identifier of an app. For details, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. For details about how to obtain **appIdentifier**, see \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ .

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DisposedRuleConfiguration-appId: string--><!--Device-DisposedRuleConfiguration-appId: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## appIndex

```TypeScript
appIndex: int
```

Index of the application clone. The default value is **0**. The value **0** means to set the disposed rule for the main application. A value greater than 0 means to set the disposed rule for the application clone with the specified index.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DisposedRuleConfiguration-appIndex: int--><!--Device-DisposedRuleConfiguration-appIndex: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## disposedRule

```TypeScript
disposedRule: DisposedRule
```

Disposal rule of the application, including the type of the ability to be started during disposal.

**Type:** DisposedRule

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DisposedRuleConfiguration-disposedRule: DisposedRule--><!--Device-DisposedRuleConfiguration-disposedRule: DisposedRule-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

