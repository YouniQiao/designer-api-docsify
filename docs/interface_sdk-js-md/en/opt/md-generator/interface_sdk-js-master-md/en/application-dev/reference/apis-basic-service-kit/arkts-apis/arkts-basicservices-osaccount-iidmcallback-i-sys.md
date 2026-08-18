# IIdmCallback (System API)

Provides callbacks for IDM.

**Since:** 23

<!--Device-osAccount-interface IIdmCallback--><!--Device-osAccount-interface IIdmCallback-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## onAcquireInfo

```TypeScript
onAcquireInfo?: (module: number, acquire: number, extraInfo: Uint8Array) => void
```

Called to acquire IDM information.

**Type:** (module: number, acquire: number, extraInfo: Uint8Array) =&gt; void

**Since:** 23

<!--Device-IIdmCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void--><!--Device-IIdmCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## onResult

```TypeScript
onResult: (result: number, extraInfo: RequestResult) => void
```

Called to return the result code and request result information.

**Type:** (result: number, extraInfo: RequestResult) =&gt; void

**Since:** 23

<!--Device-IIdmCallback-onResult: (result: int, extraInfo: RequestResult) => void--><!--Device-IIdmCallback-onResult: (result: int, extraInfo: RequestResult) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.
