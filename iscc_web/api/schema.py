# generated by datamodel-codegen:
#   filename:  openapi.yaml

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field, confloat, conint, constr


class MediaID(BaseModel):
    __root__: constr(regex=r"[a-v0-9]{13}$", min_length=13, max_length=13) = Field(
        ...,
        description="ID for an uploaded file generated by server for each upload event.",
        example="061kcmrj55fi8",
    )


class Iscc(BaseModel):
    __root__: constr(regex=r"^ISCC:[A-Z2-7]{10,73}$", min_length=15, max_length=73) = Field(
        ...,
        description=(
            "An **ISCC** in canonical representation. This is the minimal required field for a"
            " valid ISCC Metadata object."
        ),
        example="ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    )


class UploadResponse(BaseModel):
    content: Optional[str] = Field(None, example="http://localhost:8000/api/v1/media/061knt35ejv6o")
    media_id: Optional[MediaID] = None


class _Type(Enum):
    CreativeWork = "CreativeWork"
    TextDigitalDocument = "TextDigitalDocument"
    ImageObject = "ImageObject"
    AudioObject = "AudioObject"
    VideoObject = "VideoObject"


class BasicMetadata(BaseModel):
    _context: Optional[AnyUrl] = Field(
        None,
        alias="@context",
        description="The [JSON-LD](https://json-ld.org/) Context URI for ISCC metadata.",
        example="http://purl.org/iscc/context/0.4.0.jsonld",
    )
    _type: Optional[_Type] = Field(
        "CreativeWork",
        alias="@type",
        description=(
            "The type of digital content according to schema.org classes (TextDigitalDocument,"
            " ImageObject, AudioObject, VideoObject)."
        ),
    )
    _schema: Optional[AnyUrl] = Field(
        None,
        alias="$schema",
        description="The [JSON Schema](https://json-schema.org/) URI for ISCC metadata.",
        example="http://purl.org/iscc/schema/0.4.0.json",
    )
    iscc: Optional[Iscc] = None


class InlineMetadata(BaseModel):
    name: Optional[constr(max_length=128)] = Field(
        None,
        description=(
            "The title or name of the intangible creation manifested by the identified *digital"
            " content*. **Used as input for ISCC Meta-Code generation**."
        ),
        example="The Never Ending Story",
    )
    description: Optional[constr(max_length=4096)] = Field(
        None,
        description=(
            "Description of the *digital content* identified by the **ISCC**. **Used as input for"
            " ISCC Meta-Code generation**. Any user presentable text string (including Markdown"
            " text) indicative of the identity  of the referent may be used."
        ),
        example="a 1984 fantasy film co-written and directed by *Wolfgang Petersen*",
    )
    meta: Optional[constr(max_length=16384)] = Field(
        None,
        description="Subject, industry, or use-case specific metadata encoded as Data-URL.",
        example="data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0=",
    )
    creator: Optional[str] = Field(
        None,
        description="An entity primarily responsible for making the resource.",
        example="Joanne K. Rowling",
    )
    license: Optional[str] = Field(
        None,
        description="URI of license for the identified *digital content*.",
        example="https://example.com/license-terms-for-this-item",
    )
    acquire: Optional[AnyUrl] = Field(
        None,
        description=(
            "This field must contain a valid URL referring to a page showing information about how"
            " one can acquire a license for the item. This may be a page of a web shop or NFT"
            " marketplace ready for providing a license."
        ),
        example="https://example.com/buy-license-for-item-here",
    )
    credit: Optional[str] = Field(
        None,
        description=(
            "A line of text that you expect users of the image (such as Google Images) to display"
            " alongside the image."
        ),
        example="Frank Farian - Getty Images",
    )
    rights: Optional[str] = Field(
        None,
        description=(
            "Contains any necessary copyright notice and should identify the current owner of the"
            " copyright of this work with associated intellectual property rights."
        ),
        example="Copyright 2022 ISCC Foundation - www.iscc.codes",
    )


class Mode(Enum):
    text = "text"
    image = "image"
    audio = "audio"
    video = "video"
    mixed = "mixed"


class TechnicalMetadata(BaseModel):
    mode: Optional[Mode] = Field(
        None, description="The perceptual mode used to create the ISCC.", example="image"
    )
    filename: Optional[str] = Field(
        None,
        description="Filename of the referenced **digital content**",
        example="your-media-file.jpg",
    )
    filesize: Optional[int] = Field(
        None, description="File size of media asset in number of bytes."
    )
    mediatype: Optional[str] = Field(
        None,
        description=(
            "An [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml)"
            " (MIME type)"
        ),
        example="image/jpeg",
    )
    duration: Optional[int] = Field(
        None, description="Duration of audio-visual media in seconds.", example=60
    )
    fps: Optional[confloat(ge=1.0)] = Field(
        None, description="Frames per second of video assets.", example=24
    )
    width: Optional[int] = Field(
        None, description="Width of visual media in number of pixels.", example=640
    )
    height: Optional[conint(ge=1)] = Field(
        None, description="Height of visual media in number of pixels.", example=480
    )
    characters: Optional[int] = Field(
        None,
        description="Number of text characters (code points after Unicode normalization)",
        example=55689,
    )
    language: Optional[str] = Field(
        None,
        description="Primary language of content [BCP 47](https://tools.ietf.org/search/bcp47).",
        example="en-US",
    )
    thumbnail: Optional[AnyUrl] = Field(
        None,
        description=(
            "URI an autogenerated user-presentable thumbnail-image that serves as a preview of the"
            " digital content. The URI may be a Data-URL RFC2397."
        ),
        example="https://picsum.photos/200/300.jpg",
    )


class Unit(BaseModel):
    iscc_unit: Optional[str] = Field(
        None, description="Canonical representation of ISCC-UNIT", example="ISCC:AAA4RJYGHHVRCZ5T"
    )
    readable: Optional[str] = Field(
        None,
        description="Human readable version of ISCC-UNIT",
        example="META-NONE-V0-64-c8a70639eb1167b3",
    )
    hash_hex: Optional[str] = Field(
        None, description="Hex representation of ISCC-BODY", example="e1fb7dc4e3dbb4be"
    )
    hash_uint: Optional[str] = Field(
        None,
        description="Unsigned integer representation of ISCC-BODY",
        example="16283747162278048958",
    )
    hash_bits: Optional[str] = Field(
        None,
        description="Bitpattern of ISCC-BODY",
        example="1110000111111011011111011100010011100011110110111011010010111110",
    )


class IsccDetail(BaseModel):
    iscc: Optional[Iscc] = None
    readable: Optional[str] = Field(
        None,
        description="Human readable version of ISCC",
        example=(
            "ISCC-VIDEO-V0-MSDI-c8a70639eb1167b367a9c3787c65c1e582e2e662f728b4fa42485e3a0a5d2f34"
        ),
    )
    multiformat: Optional[str] = Field(
        None,
        description="Multiformats representation base64url representation of ISCC",
        example="uzAFTBsinBjnrEWezZ6nDeHxlweWC4uZi9yi0-kJIXjoKXS80",
    )
    decomposed: Optional[str] = Field(
        None,
        description="ISCC decomomposed into a dash seperated secquence of ISCC-UNITs",
        example="AAA4RJYGHHVRCZ5T-CMAWPKODPB6GLQPF-GAAYFYXGML3SRNH2-IAAUESC6HIFF2LZU",
    )
    units: Optional[List[Unit]] = Field(
        None, description="Different representations of the individial units of the ISCC"
    )


class IsccMetadata(BasicMetadata, UploadResponse, InlineMetadata, TechnicalMetadata):
    pass
