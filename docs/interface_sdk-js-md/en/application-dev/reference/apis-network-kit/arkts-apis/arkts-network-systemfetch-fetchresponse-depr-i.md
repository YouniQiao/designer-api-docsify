# FetchResponse

*Table 2** Mapping between responseType and data in success callback

| responseType | data | Description| | -------- | -------- | -------- | | N/A| string | When the type in the header returned by the server is **text/\***, **application/json**, **application/javascript**, or **application/xml**, the value is the text content.| | text | string | Text content.| | json | Object | A JSON object.|

**Since:** 3

<!--Device-unnamed-export interface FetchResponse--><!--Device-unnamed-export interface FetchResponse-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
```

## code

```TypeScript
code: number
```

Server status code.

**Type:** number

**Since:** 3

<!--Device-FetchResponse-code: number--><!--Device-FetchResponse-code: number-End-->

**System capability:** SystemCapability.Communication.NetStack

## data

```TypeScript
data: string | object
```

The type of the returned data is determined by **responseType**. For details, see the mapping between **responseType** and **data** in **success** callback.

**Type:** string \| object

**Since:** 3

<!--Device-FetchResponse-data: string | object--><!--Device-FetchResponse-data: string | object-End-->

**System capability:** SystemCapability.Communication.NetStack

## headers

```TypeScript
headers: Object
```

All headers in the response from the server.

**Type:** Object

**Since:** 3

<!--Device-FetchResponse-headers: Object--><!--Device-FetchResponse-headers: Object-End-->

**System capability:** SystemCapability.Communication.NetStack

