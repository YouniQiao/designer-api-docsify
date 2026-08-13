# RemoteValidation

```TypeScript
export type RemoteValidation = 'system' | 'skip' | ValidationCallback
```

Remote Validation Type.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-http-export type RemoteValidation = 'system' | 'skip' | ValidationCallback--><!--Device-http-export type RemoteValidation = 'system' | 'skip' | ValidationCallback-End-->

**System capability:** SystemCapability.Communication.NetStack

| Type | Description |
| --- | --- |
| 'system' | use system validation. |
| 'skip' | skip validation. |
| ValidationCallback | [since 26.0.0] use custom validation. |

