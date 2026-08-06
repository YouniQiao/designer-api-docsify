# Filter

Defines the file filtering configuration used by **listFile()**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface Filter--><!--Device-unnamed-export interface Filter-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## displayName

```TypeScript
displayName?: Array<string>
```

Locate files that fuzzy match the specified file names, which are of the OR relationship. Currently, only the wildcard * is supported.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-displayName?: Array<string>--><!--Device-Filter-displayName?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## excludeMedia

```TypeScript
excludeMedia?: boolean
```

Whether to exclude the files already in **Media**.

The value **true** means to exclude the files already in **Media**; the value **false** means not to exclude the files already in **Media**. This parameter is reserved.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-excludeMedia?: boolean--><!--Device-Filter-excludeMedia?: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## fileSizeOver

```TypeScript
fileSizeOver?: long
```

Locate files that are greater than the specified size, in bytes.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-fileSizeOver?: long--><!--Device-Filter-fileSizeOver?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## lastModifiedAfter

```TypeScript
lastModifiedAfter?: double
```

Locate files whose last modification time is the same or later than the specified time.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-lastModifiedAfter?: double--><!--Device-Filter-lastModifiedAfter?: double-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## mimeType

```TypeScript
mimeType?: Array<string>
```

Locate files that fully match the specified MIME types, which are of the OR relationship. This parameter is reserved.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-mimeType?: Array<string>--><!--Device-Filter-mimeType?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## suffix

```TypeScript
suffix?: Array<string>
```

Locate files that fully match the specified file name extensions, which are of the OR relationship.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Filter-suffix?: Array<string>--><!--Device-Filter-suffix?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

