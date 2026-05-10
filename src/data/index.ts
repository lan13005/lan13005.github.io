import { parse } from 'smol-toml';
import raw from './profile.toml?raw';

// ─── Types ───────────────────────────────────────────────────────────────────

export interface Summary {
  cv: string;
  web: string;
  llm?: string;
}

export interface Project {
  id: string;
  title: string;
  tags: string[];
  featured?: boolean;
  github?: string;
  demo?: string;
  summary: Summary;
}

export interface Experience {
  id: string;
  role: string;
  org: string;
  location?: string;
  start: Date;
  end?: Date;
  tags: string[];
  summary: Summary;
  project?: Project[];
}

export interface Social {
  kind: string;
  href: string;
  label: string;
}

export interface Cta {
  label: string;
  href: string;
  primary: boolean;
}

export interface WhatIDo {
  icon: string;
  title: string;
  blurb: string;
}

export interface Site {
  name: string;
  role: string;
  greeting: string;
  tagline: string;
  bio: string;
  og_image: string;
  meta_title: string;
  meta_description: string;
  cta: Cta[];
  social: Social[];
  what_i_do: WhatIDo[];
}

// ─── Parse ───────────────────────────────────────────────────────────────────

interface RawExperience extends Omit<Experience, 'start' | 'end'> {
  start: string;
  end?: string;
}

interface RawProfile {
  site: Site;
  experience: RawExperience[];
}

const parsed = parse(raw) as unknown as RawProfile;

export const site: Site = parsed.site;

export const experience: Experience[] = parsed.experience.map((e) => ({
  ...e,
  start: new Date(e.start),
  end: e.end ? new Date(e.end) : undefined,
}));

// ─── Helpers ─────────────────────────────────────────────────────────────────

export type ProjectWithExperience = Project & { experience: Experience };

export function getAllProjects(): ProjectWithExperience[] {
  return experience.flatMap((e) => (e.project ?? []).map((p) => ({ ...p, experience: e })));
}

export function getFeaturedProjects(): ProjectWithExperience[] {
  return getAllProjects().filter((p) => p.featured);
}
