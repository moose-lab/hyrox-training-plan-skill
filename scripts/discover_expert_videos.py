#!/usr/bin/env python3
"""Discover candidate expert videos for HYROX training, nutrition, and athlete sleep research."""

import json
import sys
from pathlib import Path

sys.path.append('/opt/.manus/.sandbox-runtime')
from data_api import ApiClient

QUERIES = [
    "Dan Plews HYROX training",
    "RMR Training HYROX training",
    "WOD Science HYROX",
    "HYROX nutrition sports dietitian",
    "Asker Jeukendrup endurance nutrition",
    "Shona Halson athlete sleep"
]


def main():
    client = ApiClient()
    output = {"queries": {}, "candidate_videos": []}

    for query in QUERIES:
        response = client.call_api(
            'Youtube/search',
            query={"q": query, "hl": "en", "gl": "US"}
        )
        contents = response.get("contents", [])
        videos = []
        for content in contents:
            if content.get("type") != "video":
                continue
            video = content.get("video", {})
            item = {
                "query": query,
                "video_id": video.get("videoId"),
                "title": video.get("title"),
                "channel": video.get("channelTitle"),
                "url": f"https://www.youtube.com/watch?v={video.get('videoId')}",
                "published": video.get("publishedTimeText"),
                "duration": video.get("lengthText"),
                "views": video.get("viewCountText"),
                "description": video.get("descriptionSnippet", "")
            }
            videos.append(item)
            output["candidate_videos"].append(item)
        output["queries"][query] = videos[:10]

    output_path = Path("/home/ubuntu/hyrox-training-plan-skill/research/video-candidates.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {len(output['candidate_videos'])} candidate videos to {output_path}")


if __name__ == "__main__":
    main()
