# QueryParamObject

```TypeScript
export type QueryParamObject = Record<string, QueryParamValue | QueryParamValue[]>
```

A key-value object used to construct URL query parameters automatically. Each property name is treated as a query parameter key. Each property value may be either: - a single \_\_\_JSDOC\_LINK\_DESC\_USD\_11\_\_\_, or - an array of \_\_\_JSDOC\_LINK\_DESC\_USD\_12\_\_\_, which is expanded into repeated parameters with the same key. Serialization rules: - Keys and values are URL-encoded by the system. - A single value is serialized as one \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ pair. - An array value is serialized as multiple pairs using the same key. For example, \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ is serialized as \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_. - For array values, \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_ and \_\_\_INLINE\_CODE\_DESC\_USD\_4\_\_\_ elements are serialized as empty values without \_\_\_INLINE\_CODE\_DESC\_USD\_5\_\_\_. For example, \_\_\_INLINE\_CODE\_DESC\_USD\_6\_\_\_ is serialized as \_\_\_INLINE\_CODE\_DESC\_USD\_7\_\_\_. Order semantics: - This type represents query parameters as an object, not as an ordered list of key-value pairs. - Multiple values for the same key are supported through arrays. - However, callers must not rely on preserving an exact original pair order such as \_\_\_INLINE\_CODE\_DESC\_USD\_8\_\_\_. If strict ordering or repeated-key ordering is required, use a pre-encoded query string instead of \_\_\_JSDOC\_LINK\_DESC\_USD\_13\_\_\_. Usage notes: - Provide raw, unencoded keys and values. Do not pre-encode them. - If you need full control over the final query string format, use the \_\_\_INLINE\_CODE\_DESC\_USD\_9\_\_\_ form of \_\_\_INLINE\_CODE\_DESC\_USD\_10\_\_\_ instead.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-http-export type QueryParamObject = Record<string, QueryParamValue | QueryParamValue[]>--><!--Device-http-export type QueryParamObject = Record<string, QueryParamValue | QueryParamValue[]>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Property type:** Record<string, QueryParamValue | QueryParamValue[]>

